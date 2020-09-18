-- MySQL dump 10.13  Distrib 8.0.12, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: nickgame
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
  `create_at` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `card` tinyint(4) DEFAULT NULL,
  `buy` tinyint(4) DEFAULT NULL,
  `info` varchar(2000) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `status` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `history`
--

LOCK TABLES `history` WRITE;
/*!40000 ALTER TABLE `history` DISABLE KEYS */;
INSERT INTO `history` VALUES (1,NULL,1,0,'{\"type\": \"VIETTEL\",\"seri\": \"9545634684984\", \"code\": \"894231649749\", \"price\": 100000}',3,NULL),(2,NULL,0,1,'{\"game_code\": \"LQ-456789\", \"price\":350000}',3,NULL);
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
  `name` varchar(1500) COLLATE utf8_unicode_ci DEFAULT NULL,
  `price` bigint(50) DEFAULT NULL,
  `status` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `game_name` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `game_info` varchar(1500) COLLATE utf8_unicode_ci DEFAULT NULL,
  `code` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `create_at` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `images` varchar(2000) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nicks`
--

LOCK TABLES `nicks` WRITE;
/*!40000 ALTER TABLE `nicks` DISABLE KEYS */;
INSERT INTO `nicks` VALUES (1,'Bán nick LQ giá rẻ',100000,'Đang bán','Liên Quân','{\"rank\": \"Kim cương\", \"tuong\": 45, \"ngoc\": 60, \"da_quy\": 90}','LQ-456789',NULL,NULL,1),(2,'Nghỉ chơi bán nick',350000,'Đang bán','Liên Quân','{\"rank\": \"Kim cương\", \"tuong\": 45, \"ngoc\": 60, \"da_quy\": 90}','LQ-456780',NULL,NULL,2);
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
  `name` varchar(1500) COLLATE utf8_unicode_ci DEFAULT NULL,
  `account_tk` varchar(1500) COLLATE utf8_unicode_ci DEFAULT NULL,
  `super` tinyint(4) DEFAULT NULL,
  `ctv` tinyint(4) DEFAULT NULL,
  `enduser` tinyint(4) DEFAULT NULL,
  `create_at` varchar(1500) COLLATE utf8_unicode_ci DEFAULT NULL,
  `password` varchar(1500) COLLATE utf8_unicode_ci DEFAULT NULL,
  `money` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Hiếu Nguyễn','hieunguyen2020',1,0,0,NULL,'Admin123','100000'),(2,'Đức Nguyễn','nguyenthanhduc',0,1,0,NULL,'thanhduc2812','350000'),(3,'Xuân Tú','xuantu0101',0,0,1,NULL,'xuantu111','50000'),(7,'test','test',0,0,1,'2020-09-13 14:34:45.265012','test','0');
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

-- Dump completed on 2020-09-18 10:52:36
