<?php
error_reporting(E_ALL);
ini_set('display_errors','1');
ini_set('memory_limit' , '-1');
ini_set('max_execution_time','0');
ini_set('display_startup_errors','1');
date_default_timezone_set('Asia/Tehran');

if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';
use \danog\MadelineProto\EventHandler;
use \danog\MadelineProto\Tools;
use \danog\MadelineProto\API;
use danog\MadelineProto\Logger as MPLogger;
use danog\MadelineProto\Settings;
use danog\MadelineProto\Settings\AppInfo;
use danog\MadelineProto\Settings\Peer;
use danog\MadelineProto\Settings\Logger;
use danog\MadelineProto\Settings\Serialization;
use danog\MadelineProto\Settings\Database\Mysql as MPSql;
use \danog\MadelineProto\RPCErrorException;
use \danog\Loop\Generic\GenericLoop;
use \danog\MadelineProto\Shutdown;
use Amp\Mysql;
////////////////////////////////////////
class XHandler extends EventHandler
{
    const Admins = ["1779983531","1643608696"];//Admins list like ["123","1234","12345"]
    const Report = "1643608696"; // Report can be channel,private or group
    const Channel = '-1001518091684'; // Channel id
    const database = [
        'host' => '127.0.0.1',
        'user_name' => 'rd_root',
        'user_pass' => '4]5E,AQ1I6F%',
        'db_name' => 'rd_anti_spam'
    ];// db 1 its your db
    public static $start = 0;
    public static $db;
    public function getReportPeers()
    {
        return [self::Report];
    }
    function getStep($step='step'){
        $result = yield self::$db->query("SELECT * FROM `stats` WHERE `id`=0 LIMIT 1");
        if(yield $result->advance()){
            return $result->getCurrent()[$step];
        }else{
            return null;
        }
    }
    function getStamp($name,$step='spam'){
        $result = yield self::$db->query("SELECT * FROM `admins` WHERE `name`='{$name}' LIMIT 1");
        if(yield $result->advance()){
            return $result->getCurrent()[$step];
        }else{
            return null;
        }
    }
    function memUsage($units = false){
        $status = file_get_contents('/proc/' . getmypid() . '/status');
        $matchArr = array();
        preg_match_all('~^(VmRSS|VmSwap):\s*([0-9]+).*$~im', $status, $matchArr);
        if(!isset($matchArr[2][0]) || !isset($matchArr[2][1])){
            return false;
        }
        $size = intval($matchArr[2][0]) + intval($matchArr[2][1]);
        $unit = array('کیلوبایت','مگابایت','گیگابایت','ترابایت','پنتابایت');
        if($units){
            return @round($size/pow(1024,($i=floor(log($size,1024)))),0).' '.$unit[$i];
        }
        else{
            return @round($size/pow(1024,($i=floor(log($size,1024)))),0);
        }
    }
    public function genLoop()
    {
        if($this->memUsage(false) > (yield from $this->getStep('memoryusage'))){
            $this->logger("Restart simulation at ".date('m/d H:i:s'), MPLogger::ERROR);
            $this->restart();
        }
        
        // yield $this->messages->sendMessage([
        //     'peer'    => self::Report,
        //     'message' => 'Generic Loop Start At : ' . date('H:i:s')
        // ]);
        $channelAdminLogEventsFilter = [
            '_' => 'channelAdminLogEventsFilter', 
            'ban' => true,'kick' => true
        ];
        $channelAdminLogEventsFilter2 = [
            '_' => 'channelAdminLogEventsFilter',
            'settings' => true
        ];
        $chatAdminRights = [
            '_' => 'chatAdminRights',
            'change_info' => false,
            'post_messages' => false,
            'edit_messages' => false,
            'delete_messages' => false, 
            'ban_users' => false, 
            'invite_users' => false, 
            'add_admins' => false
        ];
        $admins = yield $this->channels->getParticipants(['channel' => self::Channel, 'filter' =>['_' => 'channelParticipantsAdmins'], 'offset' => 0, 'limit' => 25, 'hash' => 0]);
        $me = yield $this->getSelf()['id'];
        foreach ($admins['users'] as $key => $value) {
            try{
                yield from self::$db->query("INSERT INTO `admins` VALUES({$value['id']},'{$value['first_name']}',0,'0');");
            }catch(Throwable $t){
                try{
                    yield from self::$db->query("UPDATE  `admins` SET `name`={$value['first_name']} WHERE `id`={$value['first_name']}");
                }catch(Throwable $t){}
            }
            $channels_AdminLogResults = yield $this->channels->getAdminLog(['channel' => self::Channel, 'q' => '', 'events_filter' => $channelAdminLogEventsFilter , 'admins' => [$value['id']], 'max_id' => 0, 'min_id' => 0, 'limit' => 25]);
            $channels_AdminLogResults2 = yield $this->channels->getAdminLog(['channel' => self::Channel, 'q' => '', 'events_filter' => $channelAdminLogEventsFilter2 , 'admins' => [$value['id']], 'max_id' => 0, 'min_id' => 0, 'limit' => 25]);
            if(count($channels_AdminLogResults['events']) > (yield from $this->getStep('bancount'))){
                try{
                    if($value['id'] != $me){
                        yield $this->channels->editAdmin(['channel' => self::Channel, 'user_id' => $value['id'], 'admin_rights' => $chatAdminRights, 'rank' => 'string', ]);
                        yield $this->messages->sendMessage([
                            'peer'            => self::Admins[0],
                            'message'         => "➤ I Have edit the admin rights of <a href='tg://user?id={$value['id']}'>this admin</a> \n➤ Id : {$value['id']}\n➤ Name : {$value['first_name']}\n➤ Reason : Too many ban members!",
                            'parse_mode'=>'html',
                            'no_webpage'=>true
                        ]);
                    }
                }catch(Throwable $t){
                    if($t->getMessage() != "USER_CREATOR"){
                        yield $this->messages->sendMessage([
                            'peer'            => self::Admins[0],
                            'message'         => "➤ I Cant edit the admin rights of <a href='{$value['id']}'>this admin</a>!\n➤ Id : {$value['id']}\n➤ Name : {$value['first_name']}\n\nError : {$t->getMessage()}",
                            'parse_mode'=>'html',
                            'no_webpage'=>true
                        ]);
                    }
                    
                }
            }elseif(count($channels_AdminLogResults2['events']) > 0 && isset($channels_AdminLogResults2['events'][0]['action']['_'])) {
                if(isset($channels_AdminLogResults2['events'][0]['action']['_']) == "channelAdminLogEventActionToggleSignatures"){
                    try{
                        if($channels_AdminLogResults2['events'][0]['user_id'] != $me && $channels_AdminLogResults2['events'][0]['date'] > time()-3600){
                            yield $this->channels->editAdmin(['channel' => self::Channel, 'user_id' => $value['id'], 'admin_rights' => $chatAdminRights, 'rank' => 'string', ]);
                            yield $this->messages->sendMessage([
                                'peer'            => self::Admins[0],
                                'message'         => "➤ I Have edit the admin rights of <a href='tg://user?id={$value['id']}'>this admin</a> \n➤ Id : {$value['id']}\n➤ Name : {$value['first_name']}\n➤ Reason : Disable channel signatures!",
                                'parse_mode'=>'html',
                                'no_webpage'=>true
                            ]);
                            yield $this->channels->toggleSignatures(['channel' => self::Channel, 'enabled' => true ]);
                        }
                    }catch(Throwable $t){
                        if($t->getMessage() != "USER_CREATOR"){
                            yield $this->messages->sendMessage([
                                'peer'            => self::Admins[0],
                                'message'         => "➤ I Cant edit the admin rights of <a href='{$value['id']}'>this admin</a>!\n➤ Id : {$value['id']}\n➤ Name : {$value['first_name']}\n\nError : {$t->getMessage()}",
                                'parse_mode'=>'html',
                                'no_webpage'=>true
                            ]);
                        }
                        
                    }
                }
            }

        }
        return 60000;
    }
    
    public function onStart()
    {
        if(!self::$start){
            /* If you want ssl, pass as second argument an array with ssl options (an empty options array is valid too); if null is passed, ssl is not enabled either */
            $config = Mysql\ConnectionConfig::fromString("host=".self::database['host'].";user=".self::database['user_name'].";pass=".self::database['user_pass'].";db=".self::database['db_name']);
            /* use an alternative charset... Default is utf8mb4_general_ci */
            $config = $config->withCharset("utf8mb4_general_ci");
            /** @var Mysql\pool $db */
            self::$db = yield Mysql\pool($config);
            $genLoop = new GenericLoop([$this, 'genLoop'], 'update Status');
            $genLoop->start();
            
        }
        self::$start = time();
    }
    public function onUpdateNewChannelMessage($update)
    {
        if("-100{$update['message']['peer_id']['channel_id']}" != self::Channel){
            return;
        }
        $stamp = date("Y-m-d H:i:s");
        $chatAdminRights = [
            '_' => 'chatAdminRights',
            'change_info' => false,
            'post_messages' => false,
            'edit_messages' => false,
            'delete_messages' => false, 
            'ban_users' => false, 
            'invite_users' => false, 
            'add_admins' => false
        ];
        if(strtotime($stamp)-strtotime((yield $this->getstamp($update['message']['post_author'],'time'))) <= (yield $this->getStep('spamtime'))){
            $spam = yield $this->getstamp($update['message']['post_author'],'spam');
            $spam += 1;
            yield self::$db->query("UPDATE `admins` SET `spam`='$spam' WHERE `name`='{$update['message']['post_author']}';");
            if((yield $this->getstamp($update['message']['post_author'],'spam')) >= (yield $this->getStep('spamcount'))){
                $user_id = yield $this->getstamp($update['message']['post_author'],'id');
                $name = yield $this->getstamp($update['message']['post_author'],'name');
                try{
                        yield $this->channels->editAdmin(['channel' => self::Channel, 'user_id' => $user_id, 'admin_rights' => $chatAdminRights, 'rank' => 'string', ]);
                        yield $this->messages->sendMessage([
                            'peer'            => self::Admins[0],
                            'message'         => "➤ I Have edit the admin rights of <a href='tg://user?id={$user_id}'>this admin</a> \n➤ Id : {$user_id}\n➤ Name : {$name}\n➤ Reason : Spam Channel!",
                            'parse_mode'=>'html',
                            'no_webpage'=>true
                        ]);
                        $group = range($update['message']['id']-(yield $this->getstamp($update['message']['post_author'],'spam')),$update['message']['id']);
                        try{
                            yield $this->channels->deleteMessages(['channel' =>self::Channel,'id' =>$group]);                                
                            yield $this->sleep(0.1);
                        }catch(\danog\MadelineProto\RPCErrorException $e){
                        }catch(\danog\MadelineProto\Exception $e){
                        }catch(\danog\MadelineProto\TL\Conversion\Exception $e){}
                        
                }catch(Throwable $t){
                    if($t->getMessage() != "USER_CREATOR"){
                        yield $this->messages->sendMessage([
                            'peer'            => self::Admins[0],
                            'message'         => "➤ I Cant edit the admin rights of <a href='{$user_id}'>this admin</a>!\n➤ Id : {$user_id}\n➤ Name : {$name}\n\nError : {$t->getMessage()}",
                            'parse_mode'=>'html',
                            'no_webpage'=>true
                        ]);
                    }
                    
                } 
            }
        }else{
            self::$db->query("UPDATE `admins` SET `spam`='0',`time`='$stamp' WHERE `name`='{$update['message']['post_author']}';");
        }
        yield $this->onUpdateNewMessage($update);
    }
    public function onUpdateEditMessage($update){
        yield $this->onUpdateNewMessage($update);
    }
    public function onUpdateNewMessage($update)
    {
        if(self::$start && $update['message']['date'] < self::$start && $update["_"] != "updateEditChannelMessage" && $update["_"] != "updateEditMessage") {
            return;
        }
        try {
            $messageId = $update['message']['id'] ?? 0;
            $msgOrig   = $update['message']['message'] ?? null;
            $fromId    = $update['message']['from_id']['user_id'] ?? 0;
            $replyToId = $update['message']['reply_to']['reply_to_msg_id'] ?? 0;
            $peer      = yield $this->getID($update);
            @$type3 = yield $this->getInfo($update)['type'];
            $step = yield $this->getStep();
            $me = yield $this->getSelf()['id'];
            //=====================check in list admin==============================//
            if(in_array($fromId, self::Admins) && $type3 == 'user' && $fromId != $me) {
                //=====================Ping==============================//
                if(preg_match('/^[\/\#\!\.]?(ping|ربات)$/si', $msgOrig)) {
                    yield $this->messages->sendMessage([
                        'peer'            => $peer,
                        'message'         => '➤ Im Always Online!',
                        'reply_to_msg_id' => $messageId
                    ]);
                }
                //=====================Memory==============================//
                elseif(preg_match('/^[\/\#\!\.]?(memory)$/si',$msgOrig,$input)){
                    $memory = yield $this->memUsage(true);
                    yield $this->messages->sendMessage(['peer' => $peer,'reply_to_msg_id' => $messageId, 'message' => "➤ **Memory usage is $memory**",'parse_mode'=>'markdown']);
                }
                //=====================Restart==============================//
                elseif (preg_match('/^[\/\#\!\.]?(restart|ریستارت)$/si',$msgOrig)){
                    yield $this->messages->sendMessage([
                        'peer'            => $peer,
                        'message'         => '➤ **Restarted successfully**',
                        'reply_to_msg_id' => $messageId,
                        'parse_mode'=>'markdown'
                    ]);
                    $this->restart();
                }
                //=====================Info==============================//
                elseif(preg_match("/^[\/\#\!]?(info) (.*)$/i", $msgOrig,$mu) or preg_match("/^[\/\#\!]?(info)$/i", $msgOrig)){
                    if(isset($update['message']['reply_to']) && !isset($mu[2])){
                        $messages = yield $this->messages->getMessages(['id' => [$update['message']['reply_to']['reply_to_msg_id']]]);
                        $message1 = $messages['messages'][0]['fwd_from']['from_id']['user_id'] ?? null;
                        try{
                            $mee = yield $this->get_full_info($message1);
                        }catch (\Throwable $e){
                            yield $this->messages->sendMessage(['peer' => $peer,'reply_to_msg_id' => $messageId,'message' => "➤ **Sothing went wrong!**\n➤ **I cant found info about** `Forwarded message`\n➤ **maybe he close forward!**",'parse_mode'=>'markdown']);
                            return;
                        }
                    }else{
                        try{
                            $mee = yield $this->get_full_info($mu[2]);
                        }catch(Throwable $t){
                            try{
                                $mee = yield $this->get_full_info($update['message']['entities'][0]['user_id']);
                            }catch (\Throwable $e){
                                yield $this->messages->sendMessage(['peer' => $peer,'reply_to_msg_id' => $messageId,'message' => "➤ **Sothing went wrong!**\n➤ **I cant found info about** `{$mu[2]}`",'parse_mode'=>'markdown']);
                                return;
                            }   
                        }
                    }
                    $me = $mee['User'];
                    $dc_id = isset($me['photo']['dc_id'])?$me['photo']['dc_id']:"Doesn't have!";
                    $me_id = $me['id'];
                    $me_status = isset($me['status']['_'])?$me['status']['_']:"";
                    $me_bio = isset($mee['full']['about'])?$mee['full']['about']:"Doesn't have!";
                    $me_common = isset($mee['full']['common_chats_count'])?$mee['full']['common_chats_count']:"";
                    $me_name = isset($me['first_name'])?$me['first_name']:"Doesn't have!";
                    $me_uname = isset($me['username'])?"@{$me['username']}":"Doesn't have!";
                    $mes = "➤ **ID** : $me_id \n➤ **Name** : $me_name \n➤ **Username** : $me_uname \n➤ **Status** : $me_status \n➤ **Bio** : $me_bio \n➤ **Common Groups Count** : $me_common \n➤ **DC** : $dc_id";
                    yield $this->messages->sendMessage(['peer' => $peer,'reply_to_msg_id' => $messageId,'message' => $mes,'parse_mode'=>'markdown']);
                }
                //=====================Promote==============================//
                elseif(preg_match("/^[\/\#\!]?(promote) (.*)$/i", $msgOrig,$mu) or preg_match("/^[\/\#\!]?(promote)$/i", $msgOrig)){
                    if(isset($update['message']['reply_to']) && !isset($mu[2])){
                        $messages = yield $this->messages->getMessages(['id' => [$update['message']['reply_to']['reply_to_msg_id']]]);
                        $message1 = $messages['messages'][0]['fwd_from']['from_id']['user_id'] ?? null;
                        try{
                            $mee = yield $this->get_full_info($message1);
                        }catch (\Throwable $e){
                            yield $this->messages->sendMessage(['peer' => $peer,'reply_to_msg_id' => $messageId,'message' => "➤ **Sothing went wrong!**\n➤ **I cant found info about** `Forwarded message`\n➤ **maybe he close forward!**",'parse_mode'=>'markdown']);
                            return;
                        }
                    }else{
                        try{
                            $mee = yield $this->get_full_info($mu[2]);
                        }catch(Throwable $t){
                            try{
                                $mee = yield $this->get_full_info($update['message']['entities'][0]['user_id']);
                            }catch (\Throwable $e){
                                yield $this->messages->sendMessage(['peer' => $peer,'reply_to_msg_id' => $messageId,'message' => "➤ **Sothing went wrong!**\n➤ **I cant found info about** `{$mu[2]}`",'parse_mode'=>'markdown']);
                                return;
                            }   
                        }
                    }
                    $me = $mee['User'];
                    $me_id = $me['id'];
                    yield $this->messages->sendMessage(['peer' => $peer,'reply_to_msg_id' => $messageId,'message' => "➤ **Ok time to promote** `{$me_id}`
Now send me the admin rights for example
`change_info|false`
`post_messages|true`
`edit_messages|false`
`delete_messages|false`
`invite_users|true`
`add_admins|false`
`manage_call|false`
This the defualt admin rights of one admin as you say
you can change it and tab it copy to your clipboard!
in every time you can send `/cancel` to cancel operation
",'parse_mode'=>'markdown']);
                    yield self::$db->query("UPDATE `stats` SET `step`='promote|{$me_id}' WHERE `id`=0");
                }
                elseif(preg_match_all('/(\w+)\|(\w+)/si',$msgOrig,$m) && strpos($step,"promote|") !== false && !preg_match("/^[\/\#\!]?(promote)$/i", $msgOrig)){
                    yield self::$db->query("UPDATE `stats` SET `step`='none' WHERE `id`=0");
                    $id = str_replace("promote|","",$step);
                    $chatAdminRights = ['_' => 'chatAdminRights'];
                    foreach ($m[1] as $key => $value) {
                        $chatAdminRights[$value] = filter_var($m[2][$key], FILTER_VALIDATE_BOOLEAN);
                    }
                    try{
                        yield $this->channels->editAdmin(['channel' => self::Channel, 'user_id' => $id, 'admin_rights' => $chatAdminRights, 'rank' => '', ]);
                        yield $this->messages->sendMessage(['peer' => $peer,'reply_to_msg_id' => $messageId,'message' => "➤ **Successfully promote** `{$id}`",'parse_mode'=>'markdown']);
                    }catch(Throwable $t){
                        yield $this->messages->sendMessage(['peer' => $peer,'reply_to_msg_id' => $messageId,'message' => "➤ **Sothing went wrong!**\n➤ **I cant promote** `{$id}`\n➤ **Is he join channel?!**\n➤ Error : {$t->getMessage()}",'parse_mode'=>'markdown']);

                    }
                }
                //=====================demote==============================//
                elseif(preg_match("/^[\/\#\!]?(demote) (.*)$/i", $msgOrig,$mu) or preg_match("/^[\/\#\!]?(promote)$/i", $msgOrig)){
                    if(isset($update['message']['reply_to']) && !isset($mu[2])){
                        $messages = yield $this->messages->getMessages(['id' => [$update['message']['reply_to']['reply_to_msg_id']]]);
                        $message1 = $messages['messages'][0]['fwd_from']['from_id']['user_id'] ?? null;
                        try{
                            $mee = yield $this->get_full_info($message1);
                        }catch (\Throwable $e){
                            yield $this->messages->sendMessage(['peer' => $peer,'reply_to_msg_id' => $messageId,'message' => "➤ **Sothing went wrong!**\n➤ **I cant found info about** `Forwarded message`\n➤ **maybe he close forward!**",'parse_mode'=>'markdown']);
                            return;
                        }
                    }else{
                        try{
                            $mee = yield $this->get_full_info($mu[2]);
                        }catch(Throwable $t){
                            try{
                                $mee = yield $this->get_full_info($update['message']['entities'][0]['user_id']);
                            }catch (\Throwable $e){
                                yield $this->messages->sendMessage(['peer' => $peer,'reply_to_msg_id' => $messageId,'message' => "➤ **Sothing went wrong!**\n➤ **I cant found info about** `{$mu[2]}`",'parse_mode'=>'markdown']);
                                return;
                            }   
                        }
                    }
                    $me = $mee['User'];
                    $me_id = $me['id'];
                    $chatAdminRights = [
                        '_' => 'chatAdminRights',
                        'change_info' => false,
                        'post_messages' => false,
                        'edit_messages' => false,
                        'delete_messages' => false, 
                        'ban_users' => false, 
                        'invite_users' => false, 
                        'add_admins' => false
                    ];
                    try{
                        yield $this->channels->editAdmin(['channel' => self::Channel, 'user_id' => $me_id, 'admin_rights' => $chatAdminRights, 'rank' => '', ]);
                        yield $this->messages->sendMessage(['peer' => $peer,'reply_to_msg_id' => $messageId,'message' => "➤ **Successfully demote** `{$me_id}`",'parse_mode'=>'markdown']);
                    }catch(Throwable $t){
                        yield $this->messages->sendMessage(['peer' => $peer,'reply_to_msg_id' => $messageId,'message' => "➤ **Sothing went wrong!**\n➤ **I cant demote** `{$me_id}`\n➤ **Is he join channel?!**",'parse_mode'=>'markdown']);

                    }
                }
                //=====================setspamcount==============================//
                elseif(preg_match("/^[\/\#\!]?(setspamcount) (\d+)$/i", $msgOrig,$m)){
                    yield self::$db->query("UPDATE `stats` SET `spamcount`='{$m[2]}' WHERE `id`=0");
                    yield $this->messages->sendMessage(['peer' => $peer,'reply_to_msg_id' => $messageId,'message' => "➤ **Spamcount successfully changed to** `{$m[2]}`",'parse_mode'=>'markdown']);

                }
                //=====================setspamtime==============================//
                elseif(preg_match("/^[\/\#\!]?(setspamtime) (\d+)$/i", $msgOrig,$m)){
                    yield self::$db->query("UPDATE `stats` SET `spamtime`='{$m[2]}' WHERE `id`=0");
                    yield $this->messages->sendMessage(['peer' => $peer,'reply_to_msg_id' => $messageId,'message' => "➤ **Spamtime successfully changed to** `{$m[2]}` **seconds**",'parse_mode'=>'markdown']);

                }
                //=====================setbancount==============================//
                elseif(preg_match("/^[\/\#\!]?(setbancount) (\d+)$/i", $msgOrig,$m)){
                    yield self::$db->query("UPDATE `stats` SET `bancount`='{$m[2]}' WHERE `id`=0");
                    yield $this->messages->sendMessage(['peer' => $peer,'reply_to_msg_id' => $messageId,'message' => "➤ **Bancount successfully changed to** `{$m[2]}`",'parse_mode'=>'markdown']);

                }
                //=====================setmemoryusage==============================//
                elseif(preg_match("/^[\/\#\!]?(setmemoryusage) (\d+)$/i", $msgOrig,$m)){
                    yield self::$db->query("UPDATE `stats` SET `memoryusage`='{$m[2]}' WHERE `id`=0");
                    yield $this->messages->sendMessage(['peer' => $peer,'reply_to_msg_id' => $messageId,'message' => "➤ **Memoryusage successfully changed to** `{$m[2]}` **Mb**",'parse_mode'=>'markdown']);

                }
                //=====================cancel==============================//
                elseif(preg_match("/^[\/\#\!]?(cancel)$/i", $msgOrig)){
                    yield self::$db->query("UPDATE `stats` SET `step`='none' WHERE `id`=0");
                    yield $this->messages->sendMessage(['peer' => $peer,'reply_to_msg_id' => $messageId,'message' => "➤ **Operation canceled successfully**",'parse_mode'=>'markdown']);

                }
                //=====================Exit==============================//
                elseif(preg_match('/^[\/\#\!\.]?(exit|خروج)$/si',$msgOrig))
                {
                    yield $this->messages->sendMessage([
                            'peer'            => $peer,
                            'message'         => "➤ **Robot were Shutdown in next 3 seocnds you can cancel this operation using** `restart`",
                            'reply_to_msg_id' => $messageId,
                            'parse_mode'      => 'markdown'
                    ]);
                    yield $this->sleep(3);
                    $this->stop();
                    exit;
                }
                //=====================Help==============================//
                elseif(preg_match("/^[\/\#\!]?(help)$/i", $msgOrig)){
                    yield $this->messages->sendMessage(['peer' => $peer,'reply_to_msg_id' => $messageId,'message' => "
➤ **Help Menu** ↓
➤ `ping` | `ربات` (گرفتن جواب از سمت ربات این که انلاینه یا نه)
➤ `memory` (مقدار مصرف رم رو میگه)
➤ `restart` | `ریستارت` (ریستارت ربات)
➤ `promote` `[username]|[userid]|[reply on forwarded message]` (ادمین چنل میکنه)
➤ `demote` `[username]|[userid]|[reply on forwarded message]` (عزل میکنه)
➤ `cancel` (کنسل میکنه کار فعلی رو)
➤ `info` `[username]|[userid]|[reply on forwarded message]` (تمام اطلاعات رو درباره اون کاربر میگه)
➤ `setspamcount` `[numbers]` (تعداد اسپمو تنظیم میکنه)
➤ `setspamtime` `[seconds]` (تایم اسپمو تنظیم میکنه به ثانیه)
➤ `setbancount` `[numbers]` (تعداد بنو تنظیم میکنه)
➤ `setmemoryusage` `[numbers]` (مقدار رم مصرفی که وقتی رسید به اون مقدار ربات ریستارت بشه تنظیم میکنه به مگابایت)
➤ `exit` (ربات از اکانت خارج میشه اما با باز کردن لینک دوباره برمیگرده)",'parse_mode'=>'markdown']);

                }
            }
        } catch (\Throwable $e){
            $this->report("Surfaced: $e");
        }
        try{
            try{
                yield $this->channels->readHistory(['channel' => $update, 'max_id' => $messageId]);
            }catch(Throwable $t){
                yield $this->messages->readHistory(['peer' => $update, 'max_id' => $messageId]);
            }
        } catch (\Throwable $e){
            $this->report("Surfaced: $e");
        }
    }
}
$Mddb = (new MPSql)
    ->setUri('tcp://localhost')
    ->setUsername('rd_root') 
    ->setPassword('4]5E,AQ1I6F%')
    ->setDatabase('rd_anti_spam')
    ->setMaxConnections(30)
;// db2 its madeline db

$app = (new AppInfo)
    ->setApiId(14714666) // (int) Api id
    ->setApiHash('06a116b26d84683e08764df598dc36ce') // (string)Api hash
;//Api hash & Api id

$Mdpeer = (new Peer)
    ->setFullFetch(false)
    ->setCacheAllPeersOnStartup(false)
    ->setFullInfoCacheTime(60)
;

$logger = (new Logger)
    ->setLevel(MPLogger::FILE_LOGGER)
    ->setMaxSize(1024 * 100)
;

$serialization = (new Serialization)
    ->setInterval(60)
;

$settings = new Settings;
$settings->setDb($Mddb);
$settings->setAppInfo($app);
$settings->setPeer($Mdpeer);
$settings->setLogger($logger);
$settings->setSerialization($serialization);

$settings->getFiles()->setUploadParallelChunks(100);

$bot = new API('AntiSpam.session', $settings);
$bot->startAndLoop(XHandler::class);
?>