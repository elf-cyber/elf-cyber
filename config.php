<?php
header('Content-Type: application/json; charset=utf-8');
$Server = "127.0.0.1";
$user = "rd_root";//Db username
$pass = "4]5E,AQ1I6F%";//Db password
$dbName = "rd_anti_spam";//Db name
$dsn = "mysql:host=$Server;dbname=$dbName;charset=utf8mb4";
mb_internal_encoding('UTF-8');
mb_http_output('UTF-8');
try{
    $db = new PDO($dsn,$user,$pass,array(
        PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES utf8"
      ));
    $db->setAttribute(PDO::ERRMODE_EXCEPTION,PDO::ATTR_EMULATE_PREPARES);
    $db->exec("CREATE TABLE `admins` (
            `id` INT PRIMARY KEY,
            `name` VARCHAR(200),
            `spam` INT,
            `time` VARCHAR(200))
            CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
        CREATE TABLE `stats` (
            `id` INT PRIMARY KEY,
            `step` VARCHAR(200),
            `spamtime` INT,
            `spamcount` INT,
            `memoryusage` INT,
            `bancount` INT)
            CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
        INSERT INTO `stats` (`id`,`step`,`spamtime`,`spamcount`,`memoryusage`,`bancount`) VALUES(0,'none',10,10,90,10);");
        echo json_encode(['ok'=>true,'coder'=>'@J_A_V_A','message'=>'Table created Succeessfully!']);
}catch (PDOException $error){
    //PDO EXCEPTION HANDLING
    echo json_encode(['ok'=>false,'coder'=>'@J_A_V_A','message'=>'Something went wrong!!'.PHP_EOL.$error->getMessage()],448);
    die();
}
