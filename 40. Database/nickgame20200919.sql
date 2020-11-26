-- MySQL dump 10.13  Distrib 8.0.12, for Win64 (x86_64)
--
-- Host: localhost    Database: nickgame
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `history`
--

DROP TABLE IF EXISTS `history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `history` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `create_at` varchar(150) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `card` tinyint(4) DEFAULT NULL,
  `buy` tinyint(4) DEFAULT NULL,
  `info` varchar(2000) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `status` varchar(150) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `history`
--

LOCK TABLES `history` WRITE;
/*!40000 ALTER TABLE `history` DISABLE KEYS */;
INSERT INTO `history` VALUES (1,NULL,1,0,'{\"type\": \"VIETTEL\",\"seri\": \"9545634684984\", \"code\": \"894231649749\", \"price\": 100000}',3,'Confirm'),(2,NULL,0,1,'{\"game_code\": \"LQ-456789\", \"price\":350000}',3,'Confirm'),(3,NULL,0,0,'{\"price\": 500000, \"description\":\"rut tien mua sua cho con\"}',2,'Processed'),(4,NULL,0,0,'{\"price\": 1000000, \"description\":\"Tien luong thang\"}',2,'Processed'),(5,'2020-10-17 09:47:36.471061',0,0,'{\"price\": \"100000\", \"description\": \"Test r\\u00fat ti\\u1ec1n\"}',2,'Confirm');
/*!40000 ALTER TABLE `history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nicks`
--

DROP TABLE IF EXISTS `nicks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `nicks` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(1500) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `price` bigint(50) DEFAULT NULL,
  `status` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `game_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `game_info` varchar(1500) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `code` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `create_at` varchar(150) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `images` varchar(2000) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nicks`
--

LOCK TABLES `nicks` WRITE;
/*!40000 ALTER TABLE `nicks` DISABLE KEYS */;
INSERT INTO `nicks` VALUES (1,'Bán nick LQ giá rẻ',100000,'Đã bán','Liên Quân','{\"account\": \"nguyenthanhduc\", \"password\": \"Thanhduc2812\", \"rank\": \"Kim C\\u01b0\\u01a1ng\", \"tuong\": \"2134\", \"skin\": \"234\", \"ngoc\": \"234\", \"da_quy\": \"234\"}','LQ-456789',NULL,'static/nicks/LQ-1601688546\\119450615_2360110970963936_1833809606104895409_n.jpg,static/nicks/LQ-1601688546\\119471788_366935637658710_6226179868808756332_n.jpg,static/nicks/LQ-1601688546\\119518687_338641064150213_5470597989906862570_n.jpg',1),(2,'Nghỉ chơi bán nick',350000,'Đang bán','Liên Quân','{\"account\": \"nguyenthanhduc\", \"password\": \"Thanhduc2812\", \"rank\": \"Kim C\\u01b0\\u01a1ng\", \"tuong\": \"2134\", \"skin\": \"234\", \"ngoc\": \"234\", \"da_quy\": \"234\"}','LQ-456780',NULL,'static/nicks/LQ-1601688546\\119450615_2360110970963936_1833809606104895409_n.jpg,static/nicks/LQ-1601688546\\119471788_366935637658710_6226179868808756332_n.jpg,static/nicks/LQ-1601688546\\119518687_338641064150213_5470597989906862570_n.jpg',2),(3,'Test Bán Nick',600000,'Error','Ngọc Rồng','{\"nickType\": null, \"server\": null, \"hanhTinh\": null, \"bongTai\": false, \"deTu\": false}','LQ-1601887031','2020-10-05 22:37:11.297036','static/nicks/LQ-1601688546\\119450615_2360110970963936_1833809606104895409_n.jpg,static/nicks/LQ-1601688546\\119471788_366935637658710_6226179868808756332_n.jpg,static/nicks/LQ-1601688546\\119518687_338641064150213_5470597989906862570_n.jpg',8),(4,'Nick Ngọc Rồng',400,'Error','Ngọc Rồng','{\"nickType\": \"T\\u1ea7m Trung\", \"server\": \"1\", \"hanhTinh\": \"Tr\\u00e1i \\u0110\\u1ea5t\", \"bongTai\": false, \"deTu\": false}','LQ-1601887044','2020-10-05 22:37:24.979389','static/nicks/LQ-1601688546\\119450615_2360110970963936_1833809606104895409_n.jpg,static/nicks/LQ-1601688546\\119471788_366935637658710_6226179868808756332_n.jpg,static/nicks/LQ-1601688546\\119518687_338641064150213_5470597989906862570_n.jpg',8),(9,'Test Bán Nick',99999999,'Đang bán','Liên Quân','{\"account\": \"nguyenthanhduc\", \"password\": \"Thanhduc2812\", \"rank\": \"Kim C\\u01b0\\u01a1ng\", \"tuong\": \"2134\", \"skin\": \"234\", \"ngoc\": \"234\", \"da_quy\": \"234\"}','LQ-1601667349','2020-10-03 09:35:49.137164','static/nicks/LQ-1601688546\\119344245_759746261424862_1470443585957313168_n.jpg',3),(10,'Test Bán Nick',9999999,'Đang bán','Liên Quân','{\"account\": \"nguyenthanhduc\", \"password\": \"Thanhduc2812\", \"rank\": \"Kim C\\u01b0\\u01a1ng\", \"tuong\": \"2134\", \"skin\": \"234\", \"ngoc\": \"234\", \"da_quy\": \"234\"}','LQ-1601668484','2020-10-03 09:54:44.058563','static/nicks/LQ-1601688546\\119344245_759746261424862_1470443585957313168_n.jpg',3),(11,'Test Bán Nick',2222,'Đang bán','Liên Quân','{\"account\": \"nguyenthanhduc\", \"password\": \"Thanhduc2812\", \"rank\": \"Kim C\\u01b0\\u01a1ng\", \"tuong\": \"2134\", \"skin\": \"234\", \"ngoc\": \"234\", \"da_quy\": \"234\"}','LQ-1601669237','2020-10-03 10:07:17.160611','static/nicks/LQ-1601688546\\119344245_759746261424862_1470443585957313168_n.jpg',3),(12,'Nick Ngọc Rồng',0,'Đang bán','Ngọc Rồng','{\"account\": \"nguyenthanhduc\", \"password\": \"Thanhduc2812\", \"nickType\": \"T\\u1ea7m Trung\", \"server\": \"1\", \"hanhTinh\": \"Tr\\u00e1i \\u0110\\u1ea5t\", \"bongTai\": null, \"deTu\": null}','LQ-1601670340','2020-10-03 10:25:40.808084','static/nicks/LQ-1601688546\\119235912_1322518571418183_2015416670891484177_n.jpg',3),(13,'Test Bán Nick',345,'Đang bán','Liên Quân','{\"account\": \"nguyenthanhduc\", \"password\": \"Thanhduc2812\", \"rank\": \"Kim C\\u01b0\\u01a1ng\", \"tuong\": \"2134\", \"skin\": \"234\", \"ngoc\": \"234\", \"da_quy\": \"234\"}','LQ-1601670818','2020-10-03 10:33:38.040299','static/nicks/LQ-1601688546\\119235912_1322518571418183_2015416670891484177_n.jpg',3),(14,'Test Bán Nick',0,'Đang bán','Liên Quân','{\"account\": \"nguyenthanhduc\", \"password\": \"Thanhduc2812\", \"rank\": \"Kim C\\u01b0\\u01a1ng\", \"tuong\": \"2134\", \"skin\": \"234\", \"ngoc\": \"234\", \"da_quy\": \"234\"}','LQ-1601671182','2020-10-03 10:39:42.995983','static/nicks/LQ-1601688546\\119235912_1322518571418183_2015416670891484177_n.jpg',3),(15,'Dế Choắt',999999,'Đang bán','Liên Quân','{\"account\": \"nguyenthanhduc\", \"password\": \"Thanhduc2812\", \"rank\": \"Kim C\\u01b0\\u01a1ng\", \"tuong\": \"2134\", \"skin\": \"234\", \"ngoc\": \"234\", \"da_quy\": \"234\"}','LQ-1601671333','2020-10-03 10:42:13.723718','static/nicks/LQ-1601688546\\119235912_1322518571418183_2015416670891484177_n.jpg',3),(16,'Phạm Văn A',999999,'Đang bán','Liên Quân','{\"account\": \"nguyenthanhduc\", \"password\": \"Thanhduc2812\", \"rank\": \"Kim C\\u01b0\\u01a1ng\", \"tuong\": \"2134\", \"skin\": \"234\", \"ngoc\": \"234\", \"da_quy\": \"234\"}','LQ-1601687441','2020-10-03 15:10:41.176946','static/nicks/LQ-1601688546\\119235912_1322518571418183_2015416670891484177_n.jpg',3),(17,'Bad boy',666666,'Đang bán','Liên Quân','{\"account\": \"nguyenthanhduc\", \"password\": \"Thanhduc2812\", \"rank\": \"Kim C\\u01b0\\u01a1ng\", \"tuong\": \"2134\", \"skin\": \"234\", \"ngoc\": \"234\", \"da_quy\": \"234\"}','LQ-1601688546','2020-10-03 15:29:06.015463','static/nicks/LQ-1601688546\\119235912_1322518571418183_2015416670891484177_n.jpg',3),(18,'Binz',999999,'Đang bán','Liên Quân','{\"account\": \"nguyenthanhduc\", \"password\": \"Thanhduc2812\", \"rank\": \"Kim C\\u01b0\\u01a1ng\", \"tuong\": \"2134\", \"skin\": \"234\", \"ngoc\": \"234\", \"da_quy\": \"234\"}','LQ-1601689608','2020-10-03 15:46:48.752935','static/nicks/LQ-1601689608\\119344245_759746261424862_1470443585957313168_n.jpg',3),(19,'Test final',666666,'Đang bán','Liên Quân','{\"account\": \"karik\", \"password\": \"ducthi12\", \"rank\": \"Kim C\\u01b0\\u01a1ng\", \"tuong\": \"66\", \"skin\": \"66\", \"ngoc\": \"66\", \"da_quy\": \"66\"}','LQ-1601698097','2020-10-03 18:08:17.412703','static/nicks/LQ-1601698097\\119235912_1322518571418183_2015416670891484177_n.jpg',3),(20,'test ngọc rồng',9999999,'Đang bán','Ngọc Rồng','{\"nickType\": \"T\\u1ea7m Trung\", \"server\": \"4\", \"hanhTinh\": \"Tr\\u00e1i \\u0110\\u1ea5t\", \"bongTai\": null, \"deTu\": null}','LQ-1601699194','2020-10-03 18:26:34.627611','static/nicks/LQ-1601699194\\119251787_357970885359676_6440058146804173413_n.jpg',8),(21,'ddd',34234,'Đang bán','Ngọc Rồng','{\"nickType\": \"S\\u01a1 Sinh\", \"server\": \"3\", \"hanhTinh\": \"Tr\\u00e1i \\u0110\\u1ea5t\", \"bongTai\": null, \"deTu\": null}','LQ-1601699648','2020-10-03 18:34:08.222679','static/nicks/LQ-1601699648\\119489722_266036701431664_5290667515652529461_n.jpg',8),(22,'dđaa',243,'Đang bán','Ngọc Rồng','{\"nickType\": \"T\\u1ea7m Trung\", \"server\": \"8\", \"hanhTinh\": \"Tr\\u00e1i \\u0110\\u1ea5t\", \"bongTai\": \"on\", \"deTu\": \"on\"}','LQ-1601699716','2020-10-03 18:35:16.972280','static/nicks/LQ-1601699716\\119412170_245530086742745_1106787328744527221_n.jpg',8),(23,'ooooooooooo',234,'Đang bán','Ngọc Rồng','{\"nickType\": \"T\\u1ea7m Trung\", \"server\": \"3\", \"hanhTinh\": \"Tr\\u00e1i \\u0110\\u1ea5t\", \"bongTai\": true, \"deTu\": true}','LQ-1601699783','2020-10-03 18:36:23.207679','static/nicks/LQ-1601699783\\119251787_357970885359676_6440058146804173413_n.jpg',8),(24,'test edit 1',23211,'Đang bán','Ngọc Rồng','{\"nickType\": null, \"server\": null, \"hanhTinh\": null, \"bongTai\": false, \"deTu\": false}','LQ-1601701229','2020-10-03 19:00:29.874658','static/nicks/LQ-1601701229\\119251787_357970885359676_6440058146804173413_n.jpg',8),(25,'test A',9999999,'Xác nhận','Liên Quân','{\"account\": \"nguyenthanhduc\", \"password\": \"thanhduc2812\", \"rank\": \"Th\\u00e1ch \\u0111\\u1ea5u\", \"tuong\": \"60\", \"skin\": \"40\", \"ngoc\": \"50\", \"da_quy\": \"51\"}','LQ-1602051027','2020-10-07 20:10:27.520959','static/nicks/LQ-1602051027\\119344245_759746261424862_1470443585957313168_n.jpg,static/nicks/LQ-1602051027\\119450615_2360110970963936_1833809606104895409_n.jpg,static/nicks/LQ-1602051027\\119471788_366935637658710_6226179868808756332_n.jpg,static/nicks/LQ-1602051027\\119518687_338641064150213_5470597989906862570_n.jpg',8),(26,'Test B',6666666,'Đang bán','Ngọc Rồng','{\"nickType\": \"Th\\u01b0\\u1eddng\", \"server\": \"5\", \"hanhTinh\": \"Tr\\u00e1i \\u0110\\u1ea5t\", \"bongTai\": false, \"deTu\": false}','NR-1602051195','2020-10-07 20:13:15.131694','static/nicks/NR-1602051119\\119251787_357970885359676_6440058146804173413_n.jpg',8),(27,'Test ban nick',600000,'Xác nhận','Liên Quân','{\"account\": \"nguyenthanhduc\", \"password\": \"thanhduc2812\", \"rank\": \"5\", \"tuong\": \"6\", \"skin\": \"4\", \"ngoc\": \"9\", \"da_quy\": \"7\"}','LQ-1602360813','2020-10-11 10:13:33.958551','static/nicks/LQ-1602360813\\119471788_366935637658710_6226179868808756332_n.jpg,static/nicks/LQ-1602360813\\119518687_338641064150213_5470597989906862570_n.jpg',2);
/*!40000 ALTER TABLE `nicks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `users` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(1500) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `account_tk` varchar(1500) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `super` tinyint(4) DEFAULT NULL,
  `ctv` tinyint(4) DEFAULT NULL,
  `enduser` tinyint(4) DEFAULT NULL,
  `create_at` varchar(1500) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `password` varchar(1500) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `money` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `status` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Hiếu Nguyễn','hieunguyen2020',1,0,0,NULL,'Admin123','100000',NULL),(2,'Đức Nguyễn','nguyenthanhduc',0,1,0,NULL,'thanhduc2812','250000',NULL),(3,'Xuân Tú','xuantu0101',0,0,1,NULL,'xuantu111','50000',NULL),(7,'test','test',0,0,1,'2020-09-13 14:34:45.265012','test','0',NULL),(8,'Admin','admin',1,NULL,NULL,NULL,'Thanhduc2812','1000000',NULL),(9,'Phạm Văn A','phamvana',0,1,0,'2020-09-29 20:44:25.017572','1',NULL,NULL),(10,'Nguyễn B','bnguyen',0,1,0,'2020-09-29 20:45:17.970970','2',NULL,NULL),(11,'aaaaaa','aaaaaaaaaa',0,1,0,'2020-10-07 21:26:10.611856','a','90',NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-26 21:15:23
