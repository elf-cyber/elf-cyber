<?php
# Coded By AmiR
error_reporting(E_ALL);
ignore_user_abort(true);
ini_set('memory_limit', '-1');
ini_set('display_errors', '1');
ini_set('max_execution_time', '0');
ini_set('display_startup_errors', '1');
date_default_timezone_set('Asia/Tehran');
use danog\MadelineProto\{API,EventHandler,Exception,Logger as MPLogger,RPCErrorException,Settings};
use danog\MadelineProto\Settings\{AppInfo,Serialization,Logger};
use function \Amp\File\{get,put};
if (!file_exists('setting.json')) : file_put_contents('setting.json',json_encode(['Admins'=>[],'Linkdoni'=>[],'PvAuto'=>'On','JoinAuto'=>'On'])); file_put_contents('dbuser.json',json_encode([])); file_put_contents('msg.json',json_encode([])); endif;
if (file_exists('./vendor/autoload.php')) {include './vendor/autoload.php';}else{if (!file_exists($phar = 'madeline.php') or filesize($phar) < 5000){copy('https://phar.madelineproto.xyz/madeline.php', $phar);}include $phar;}
const Config = [
    'Report' => '', # Report To Username
    'Api_Hash'=>[
        'Api_Hash'=>'a42b7a458a41ca52f7812a52f76bc561', # API Hash
        'Api_Id'=>16628384 # API iD
    ],
    'ADMIN'=>5179224203, # Admin iD
    'Acc' => 1 # Account Count
];
const MSS = json_decode(file_get_contents('msg.json'));
define('PO',PHP_EOL);
class AmiR extends EventHandler
{
    public function getReportPeers() { return [Config['Report']];}
    public function Settings() {
        return json_decode(get('setting.json'));
    }
    public function onStart(){}
    public function onUpdateNewChannelMessage(array $update): Generator{ yield from $this->onUpdateNewMessage($update); }
    public function onUpdateNewMessage(array $update): Generator
    {
        if ($update['message']['_'] === 'messageService' || $update['message']['_'] === 'messageEmpty'  || time() - $update['message']['date'] > 1) {}else{
        try 
        {
            $userID = $update['message']['from_id']['user_id'] ?? 0;$msg = $update['message']['message'] ?? null;$message = isset($update['message']) ? $update['message'] : '';$msg_id = $update['message']['id'] ?? 0;$replyToId = $update['message']['reply_to']['reply_to_msg_id'] ?? 0;$getInfo = yield $this->getInfo($update);$type = $getInfo['type'];$Me = yield $this->getSelf();$chatID = yield $this->getID($update);if (($userID != Config['ADMIN'] or !in_array($userID,json_decode(get('setting.json'))['Admins']) ) and $chatID != Config['GROUP_MANAGE']) { $mem_using = round((memory_get_usage()/1024)/1024, 0); if($mem_using > 100){ $this->restart(); } }
            if (($userID == Config['ADMIN'] or in_array($userID,json_decode(get('setting.json'))['Admins']) )) :
                if ($msg == 'Bot' or $msg == 'ربات') :
                    yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'📡 Bot iS On !']);
                elseif ($msg == 'GetInfo') :
                    $Msg = yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Please Wait . . .'])['updates'][0];
                    $Contacts = yield $this->contacts->getContacts()['saved_count'];
                    $Dialogs = yield $this->getDialogs();
                    $Di = ['Channel'=>0,'PV'=>0,'Group'=>0,'Bot'=>0];
                    foreach ($Dialogs as $D) :
                        $D = yield $this->getInfo($D);
                        if ($D['type'] == 'supergroup' or $D['type'] == 'chat') :
                            $Di['Group'] = $Di['Group'] + 1;
                        elseif ($D['type'] == 'channel') :
                            $Di['Channel'] = $Di['Channel'] + 1;
                        elseif ($D['type'] == 'user') :
                            $Di['PV'] = $Di['PV'] + 1;
                        elseif ($D['type'] == 'bot') :
                            $Di['Bot'] = $Di['Bot'] + 1;
                        endif;
                    endforeach;
                    yield $this->messages->editMessage(['peer'=>$chatID,'message'=>"ID : {$Me['id']}\nContact Count : {$Contacts}\nPV Count : {$Di['PV']}\nGroup Count : {$Di['Group']}\nChannel Count : {$Di['Channel']}\nBot Count : {$Di['Bot']}\nAll Pv Count : ".count($Dialogs)."\nPhone Number : {$Me['phone_number']}",'id'=>$Msg['id']]);
                    unset($Msg,$Contacts,$Di,$Dialogs,$D);
                elseif (strpos($msg,'SaveContact') !== False) :
                    $Str = str_replace('SaveContact ','',$msg);
                    $Msg = yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Please Wait . . .'])['updates'][0];
                    try {
                        yield $this->channels->joinChannel(['channel'=>$Str]);
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Joined To Chat Secufully !','id'=>$Msg['id']]);
                    }catch (\Throwable $e) { 
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Error To Join Chat !'.PO.'Error : '.$e->getMessage(),'id'=>$Msg['id']]);
                        yield $this->restart();
                    }
                    try {
                        $Pwr = yield $this->getPwrChat($Str);
                        $i = 0;
                        foreach ($Pwr['participants'] as $P) :
                            try { yield $this->contacts->addContact(['id'=>$P['user']['id'],'first_name'=>rand(1,9999999),'last_name'=>rand(1,999999999999)]);$i = $i + 1;}
                            catch (\Throwable $e) {
                                yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Error To Save Cotacts !'.PO.'Error : '.$e->getMessage(),'id'=>$Msg['id']]);
                                yield $this->restart();
                                break;
                            }
                        endforeach;
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Secufully Save Member'.PO.'Count : '.$i,'id'=>$Msg['id']]);
                    }catch (\Throwable $e) {
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Error To Get Memver List !'.PO.'Error : '.$e->getMessage(),'id'=>$Msg['id']]);
                        yield $this->restart();
                    }
                    unset($Str,$Msg,$Pwr,$i,$e,$P);
                elseif (strpos('SaveMemberToDB',$msg) !== False) :
                    $Str = str_replace('SaveMemberToDB ','',$msg);
                    $Msg = yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Please Wait . . .'])['updates'][0];
                    try {
                        yield $this->channels->joinChannel(['channel'=>$Str]);
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Joined To Chat Secufully !','id'=>$Msg['id']]);
                    }catch (\Throwable $e) { 
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Error To Join Chat !'.PO.'Error : '.$e->getMessage(),'id'=>$Msg['id']]);
                        yield $this->restart();
                    }
                    try {
                        $Pwr = yield $this->getPwrChat($Str);
                        $i = 0;
                        $Mem = json_decode(get('dbuser.json'));
                        foreach ($Pwr['participants'] as $P) :
                            try {$Mem[$Str][] = $P['user']['id'];$i = $i + 1;}
                            catch (\Throwable $e) {
                                yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Error To Save Members !'.PO.'Error : '.$e->getMessage(),'id'=>$Msg['id']]);
                                yield $this->restart();
                                break;
                            }
                        endforeach;
                        put('dbuser.json',json_encode($Mem));
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Secufully Save Member'.PO.'Count : '.$i,'id'=>$Msg['id']]);
                    }catch (\Throwable $e) {
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Error To Get Memver List !'.PO.'Error : '.$e->getMessage(),'id'=>$Msg['id']]);
                        yield $this->restart();
                    }
                    unset($Str,$Msg,$Pwr,$i,$e,$P,$Mem);
                elseif (strpos('AddContactToGroup',$msg) !== False) :
                    $Str = explode(' ',str_replace('AddContactToGroup ','',$msg));
                    $Msg = yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Please Wait . . .'])['updates'][0];
                    try {
                        yield $this->channels->joinChannel(['channel'=>$Str[0]]);
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Joined To Chat Secufully !','id'=>$Msg['id']]);
                    }catch (\Throwable $e) { 
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Error To Join Chat !'.PO.'Error : '.$e->getMessage(),'id'=>$Msg['id']]);
                        unset($e);
                        yield $this->restart();
                    }
                    try {
                        $i = [0,0];
                        $Con = yield $this->contacts->getContacts(['hash' => ''])['users'];
                        foreach ($Con as $C) :
                            if ($i[1] >= $Str[1]) :
                                break;
                            endif;
                            try { yield $this->channels->inviteToChannel(['channel'=>$Str[0],'users'=>[$C['id']]]); $i[0] = $i[0] + 1;}
                            catch (\Throwable $e) {continue;}
                            $i[1] = $i[1] + 1;
                            yield $this->sleep($Str[2]);
                        endforeach;
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Added '.$i[0].' To Group !','id'=>$Msg['id']]);
                        yield $this->channels->leaveChannel(['channel'=>$Str[0]]);
                    }catch (\Throwable $e) {
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Error : '.$e->getMessage(),'id'=>$Msg['id']]);
                    }
                elseif (strpos('AddPvToGroup',$msg) !== False) :
                    $Str = explode(' ',str_replace('AddPvToGroup ','',$msg));
                    $Msg = yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Please Wait . . .'])['updates'][0];
                    try {
                        yield $this->channels->joinChannel(['channel'=>$Str[0]]);
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Joined To Chat Secufully !','id'=>$Msg['id']]);
                    }catch (\Throwable $e) { 
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Error To Join Chat !'.PO.'Error : '.$e->getMessage(),'id'=>$Msg['id']]);
                        unset($e);
                        yield $this->restart();
                    }
                    try {
                        $i = [0,0];
                        $Con = yield $this->getDialogs();
                        foreach ($Con as $C) :
                            if ($i[1] >= $Str[1]) :
                                break;
                            endif;
                            try {$D = yield $this->getInfo($C); if ($D['type'] == 'user') : yield $this->channels->inviteToChannel(['channel'=>$Str[0],'users'=>[$D['id']]]); endif; $i[0] = $i[0] + 1;}
                            catch (\Throwable $e) {continue;}
                            $i[1] = $i[1] + 1;
                            yield $this->sleep($Str[2]);
                        endforeach;
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Added '.$i[0].' To Group !','id'=>$Msg['id']]);
                        yield $this->channels->leaveChannel(['channel'=>$Str[0]]);
                    }catch (\Throwable $e) {
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Error : '.$e->getMessage(),'id'=>$Msg['id']]);
                    }
                elseif (strpos('Join',$msg) !== False) :
                    try {
                        yield $this->channels->joinChannel(['channel'=>str_replace('Join','',$msg)]);
                        yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Joined !']);
                    }catch (\Throwable $e) {
                        yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Error To Join : '.$e->getMessage()]);
                        unset($e);
                    }
                elseif (strpos('ChangeName',$msg) !== False) :
                    try {
                        $Chat = explode('|',str_replace('ChangeName ','',$msg));
                        yield $this->account->updateProfile(['first_name'=>$Chat[array_rand($Chat)]]);
                        yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Name Changed !']);
                    }catch (\Throwable $e) {
                        yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Error To Name Changed : '.$e->getMessage()]);
                        unset($e);
                    }
                    unset($Chat);
                elseif (strpos('ChangeBio',$msg) !== False) :
                    try {
                        yield $this->account->updateProfile(['about'=>str_replace('ChangeBio ','',$msg)]);
                        yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Bio Changed !']);
                    }catch (\Throwable $e) {
                        yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Error To Bio Changed : '.$e->getMessage()]);
                        unset($e);
                    }
                elseif (strpos('SetPvAuto',$msg) !== False) :
                    $Str = str_replace('SetPvAuto ','',$msg);
                    if ($Str == 'On') :
                        $T = $this->Settings();
                        $T['PvAuto'] = 'On';
                        put('setting.json',json_encode($T));
                        yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'PvAuto iS On !']);
                        unset($T);
                    elseif ($Str == 'Off') :
                        $T = $this->Settings();
                        $T['PvAuto'] = 'Off';
                        put('setting.json',json_encode($T));
                        yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'PvAuto iS Off !']);
                        unset($T);
                    endif;
                elseif (strpos('SetJoinAuto',$msg) !== False) :
                    $Str = str_replace('SetJoinAuto ','',$msg);
                    if ($Str == 'On') :
                        $T = $this->Settings();
                        $T['JoinAuto'] = 'On';
                        put('setting.json',json_encode($T));
                        yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'JoinAuto iS On !']);
                        unset($T);
                    elseif ($Str == 'Off') :
                        $T = $this->Settings();
                        $T['JoinAuto'] = 'Off';
                        put('setting.json',json_encode($T));
                        yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'JoinAuto iS Off !']);
                        unset($T);
                    endif;
                elseif ($msg == 'DeleteAllContact') :
                    $Msg = yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Please Wait . . . .'])['updates'][0];
                    try {
                        $Con = yield $this->contacts->getContacts(['hash' => ''])['users'];
                        foreach ($Con as $C) :
                            try {
                                yield $this->contacts->deleteContacts(['id' => [$C['id']]]);
                            }catch (\Throwable $e) {continue;}
                        endforeach;
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Deleted !','id'=>$Msg['id']]);
                    }catch (\Throwable $e) {
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Error To : '.$e->getMessage(),'id'=>$Msg['id']]);
                    }
                    unset($e,$C,$Con,$Msg);
                elseif ($msg == 'LeaveAllChannel') :
                    $Msg = yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Please Wait . . . .'])['updates'][0];
                    try {
                        $Dialogs = yield $this->getDialogs();
                        foreach ($Dialogs as $D) :
                            $D = yield $this->getInfo($D);
                            if ($D['type'] == 'channel') :
                                yield $this->channels->leaveChannel(['channel'=>$D['id']]);
                            endif;
                        endforeach;
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Leaved All Channel !','id'=>$Msg['id']]);
                    }catch (\Throwable $e) {
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Error To : '.$e->getMessage(),'id'=>$Msg['id']]);
                    }
                    unset($e,$D,$Dialogs,$Msg);
                elseif ($msg == 'LeaveAllGroup') :
                    $Msg = yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Please Wait . . . .'])['updates'][0];
                    try {
                        $Dialogs = yield $this->getDialogs();
                        foreach ($Dialogs as $D) :
                            $D = yield $this->getInfo($D);
                            if ($D['type'] == 'chat' or $D['type'] == 'supergroup') :
                                yield $this->channels->leaveChannel(['channel'=>$D['id']]);
                            endif;
                        endforeach;
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Leaved All Group !','id'=>$Msg['id']]);
                    }catch (\Throwable $e) {
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Error To : '.$e->getMessage(),'id'=>$Msg['id']]);
                    }
                    unset($e,$D,$Dialogs,$Msg);
                elseif ($msg == 'DeleteAllPv') :
                    $Msg = yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Please Wait . . . .'])['updates'][0];
                    try {
                        $Dialogs = yield $this->getDialogs();
                        foreach ($Dialogs as $D) :
                            $D = yield $this->getInfo($D);
                            if ($D['type'] == 'user') :
                                yield $this->messages->deleteChatUser(['user_id'=>$D['id'],'revoke_history'=>True]);
                            endif;
                        endforeach;
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Deleted All Pv !','id'=>$Msg['id']]);
                    }catch (\Throwable $e) {
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Error To : '.$e->getMessage(),'id'=>$Msg['id']]);
                    }
                    unset($e,$D,$Dialogs,$Msg);
                elseif (strpos($msg,'AddAdmin') !== False) :
                    $Str = str_replace('AddAdmin','',$msg);
                    $S = $this->Settings();
                    $S['Admins'][] = $Str;
                    put('setting.json',json_encode($S));
                    yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Added !']);
                elseif (strpos($msg,'DeleteAdmin') !== False) :
                    $Str = str_replace('DeleteAdmin','',$msg);
                    $S = $this->Settings();
                    unset($S['Admins'][$Str]);
                    put('setting.json',json_encode($S));
                    yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Deleted !']);
                elseif ($msg == 'AdminList') :
                    $S = $this->Settings();
                    $x = '';
                    foreach ($S['Admins'] as $A) :
                        $x = $x."$A\n";
                    endforeach;
                    yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Admin List : '.PHP_EOL.$x]);
                elseif ($msg == 'DeleteAllAdmin') :
                    $Str = str_replace('DeleteAdmin','',$msg);
                    $S = $this->Settings();
                    foreach ($S['Admins'] as $A) :
                        unset($S['Admins'][$A]);
                    endforeach;
                    put('setting.json',json_encode($S));
                    yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Admins Deleted !']);
                elseif (strpos($msg,'SetLinkdoni') !== False) :
                    $Str = str_replace('SetLinkdoni','',$msg);
                    $S = $this->Settings();
                    $S['Linkdoni'][] = $Str;
                    put('setting.json',json_encode($S));
                    yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Seted !']);
                elseif (strpos($msg,'DeleteLinkdoni') !== False) :
                    $Str = str_replace('DeleteLinkdoni','',$msg);
                    $S = $this->Settings();
                    unset($S['Linkdoni'][$Str]);
                    put('setting.json',json_encode($S));
                    yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Seted !']);
                elseif (strpos($msg,'DeleteAllLinkdoni') !== False) :
                    $Str = str_replace('DeleteAllLinkdoni','',$msg);
                    $S = $this->Settings();
                    foreach ($S['Linkdoni'] as $A) :
                        unset($S['Linkdoni'][$A]);
                    endforeach;
                    put('setting.json',json_encode($S));
                    yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Deleted !']);
                elseif (strpos($msg,'LinkdoniList') !== False) :
                    $Str = str_replace('LinkdoniList','',$msg);
                    $S = $this->Settings();
                    $x = '';
                    foreach ($S['Linkdoni'] as $A) :
                        $x = $x."$A\n";
                    endforeach;
                    put('setting.json',json_encode($S));
                    yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Linkdoni List : '.PHP_EOL.$x]);
                elseif (strpos($msg,'SendTextToAllPv') !== False) :
                    $Msg = yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Please Wait . . . '])['updates'][0];
                    $Str = explode(' ',str_replace('SendTextToPv ','',$msg));
                    try {
                        $Dialogs = yield $this->getDialogs();
                        $i = 0;
                        foreach ($Dialogs as $D) :
                            if ($i >= $Str[1]) :
                                break;
                            endif;
                            $D = yield $this->getInfo($D);
                            if ($D['type'] == 'user') :
                                try {
                                yield $this->messages->sendMessage(['peer'=>$D['id'],'message'=>$Str[0]]);
                                }catch (\Throwable $e) {break;}
                            endif;
                            $i = $i + 1;
                            yield $this->sleep($Str[2]);
                        endforeach;
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Sended To '.$i.' !','id'=>$Msg['id']]);
                    }catch (\Throwable $e) {
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Error To : '.$e->getMessage(),'id'=>$Msg['id']]);
                    }
                elseif (strpos($msg,'SendTextToAllGroup') !== False) :
                    $Msg = yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Please Wait . . . '])['updates'][0];
                    $Str = explode(' ',str_replace('SendTextToAllGroup ','',$msg));
                    try {
                        $Dialogs = yield $this->getDialogs();
                        $i = 0;
                        foreach ($Dialogs as $D) :
                            if ($i >= $Str[1]) :
                                break;
                            endif;
                            $D = yield $this->getInfo($D);
                            if ($D['type'] == 'supergroup' or $D['type'] == 'chat') :
                                try {
                                yield $this->messages->sendMessage(['peer'=>$D['id'],'message'=>$Str[0]]);
                                }catch (\Throwable $e) {break;}
                            endif;
                            $i = $i + 1;
                            yield $this->sleep($Str[2]);
                        endforeach;
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Sended To '.$i.' !','id'=>$Msg['id']]);
                    }catch (\Throwable $e) {
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Error To : '.$e->getMessage(),'id'=>$Msg['id']]);
                    }
                elseif (strpos($msg,'SendTextToAll') !== False) :
                    $Msg = yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Please Wait . . . '])['updates'][0];
                    $Str = explode(' ',str_replace('SendTextToAll ','',$msg));
                    try {
                        $Dialogs = yield $this->getDialogs();
                        $i = 0;
                        foreach ($Dialogs as $D) :
                            if ($i >= $Str[1]) :
                                break;
                            endif;
                            $D = yield $this->getInfo($D);
                            if ($D['type'] == 'supergroup' or $D['type'] == 'chat' or $D['type'] == 'user') :
                                try {
                                yield $this->messages->sendMessage(['peer'=>$D['id'],'message'=>$Str[0]]);
                                }catch (\Throwable $e) {break;}
                            endif;
                            $i = $i + 1;
                            yield $this->sleep($Str[2]);
                        endforeach;
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Sended To '.$i.' !','id'=>$Msg['id']]);
                    }catch (\Throwable $e) {
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Error To : '.$e->getMessage(),'id'=>$Msg['id']]);
                    }
                elseif (strpos($msg,'ForwardToAll') !== False) :
                    $Msg = yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Please Wait . . . '])['updates'][0];
                    $Str = explode(' ',str_replace('ForwardToAll ','',$msg));
                    try {
                        $Dialogs = yield $this->getDialogs();
                        $i = 0;
                        foreach ($Dialogs as $D) :
                            if ($i >= $Str[1]) :
                                break;
                            endif;
                            $D = yield $this->getInfo($D);
                            if ($D['type'] == 'supergroup' or $D['type'] == 'chat' or $D['type'] == 'user') :
                                try {
                                    yield $this->messages->forwardMessages(['from_peer' => $chatID, 'to_peer' => $D['id'], 'id' => [$replyToId]]);
                                }catch (\Throwable $e) {break;}
                            endif;
                            $i = $i + 1;
                            yield $this->sleep($Str[2]);
                        endforeach;
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Forwarded To '.$i.' !','id'=>$Msg['id']]);
                    }catch (\Throwable $e) {
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Error To : '.$e->getMessage(),'id'=>$Msg['id']]);
                    }
                elseif (strpos($msg,'ForwardToAllPv') !== False) :
                    $Msg = yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Please Wait . . . '])['updates'][0];
                    $Str = explode(' ',str_replace('ForwardToAllPv ','',$msg));
                    try {
                        $Dialogs = yield $this->getDialogs();
                        $i = 0;
                        foreach ($Dialogs as $D) :
                            if ($i >= $Str[1]) :
                                break;
                            endif;
                            $D = yield $this->getInfo($D);
                            if ($D['type'] == 'user') :
                                try {
                                    yield $this->messages->forwardMessages(['from_peer' => $chatID, 'to_peer' => $D['id'], 'id' => [$replyToId]]);
                                }catch (\Throwable $e) {break;}
                            endif;
                            $i = $i + 1;
                            yield $this->sleep($Str[2]);
                        endforeach;
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Forwarded To '.$i.' !','id'=>$Msg['id']]);
                    }catch (\Throwable $e) {
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Error To : '.$e->getMessage(),'id'=>$Msg['id']]);
                    }
                elseif (strpos($msg,'ForwardToAllGroup') !== False) :
                    $Msg = yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Please Wait . . . '])['updates'][0];
                    $Str = explode(' ',str_replace('ForwardToAllGroup ','',$msg));
                    try {
                        $Dialogs = yield $this->getDialogs();
                        $i = 0;
                        foreach ($Dialogs as $D) :
                            if ($i >= $Str[1]) :
                                break;
                            endif;
                            $D = yield $this->getInfo($D);
                            if ($D['type'] == 'supergroup' or $D['type'] == 'chat') :
                                try {
                                    yield $this->messages->forwardMessages(['from_peer' => $chatID, 'to_peer' => $D['id'], 'id' => [$replyToId]]);
                                }catch (\Throwable $e) {break;}
                            endif;
                            $i = $i + 1;
                            yield $this->sleep($Str[2]);
                        endforeach;
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Forwarded To '.$i.' !','id'=>$Msg['id']]);
                    }catch (\Throwable $e) {
                        yield $this->messages->editMessage(['peer'=>$chatID,'message'=>'Error To : '.$e->getMessage(),'id'=>$Msg['id']]);
                    }
                elseif ($msg == 'GetServerInfo') :
                    yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'Load Server : '.sys_getloadavg()]);
                elseif ($msg == 'Restart') :
                    yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>'OK !']);
                    yield $this->restart();
                endif;
            endif;
            if($type == 'supergroup') : if (yield $this->channels->getChannels(['id' => [$chatID]])['chats'][0]['banned_rights']['send_messages'] == 1) : yield $this->channels->leaveChannel(['channel' => $chatID]); endif; endif;
            if (isset(MSS[$msg]) and $type == 'private') :
                yield $this->messages->sendMessage(['peer'=>$chatID,'message'=>MSS[$msg]]);
            endif;
        } catch (\Throwable $e) {$this->report('Error : '.$e->getMessage());unset($e);}}}}
$app = (new AppInfo)->setApiId(Config['Api_Hash']['Api_Id'])->setApiHash(Config['Api_Hash']['Api_Hash']);
$logger = (new Logger)->setLevel(MPLogger::FILE_LOGGER)->setMaxSize(1024 * 100);
$serialization = (new Serialization)->setInterval(60);
$settings = new Settings;
$settings->setAppInfo($app);
$settings->setLogger($logger);
$settings->setSerialization($serialization);
$settings->getFiles()->setUploadParallelChunks(100);
foreach (range(1,Config['Acc']) as $File) :
    $Client[] = new API($File.'.madeline', $settings);
endforeach;
API::startAndLoopMulti($Client, AmiR::class);
# Coded By AmiR
?>