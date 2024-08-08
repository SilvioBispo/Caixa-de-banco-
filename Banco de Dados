-- MariaDB dump 10.19  Distrib 10.4.28-MariaDB, for Win64 (AMD64)
--
-- Host: 127.0.0.1    Database: caixaecono
-- ------------------------------------------------------
-- Server version	10.4.28-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cadastro`
--

DROP TABLE IF EXISTS `cadastro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cadastro` (
  `nome` varchar(30) DEFAULT NULL,
  `cpf` float DEFAULT NULL,
  `id` int(4) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=653 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cadastro`
--

LOCK TABLES `cadastro` WRITE;
/*!40000 ALTER TABLE `cadastro` DISABLE KEYS */;
INSERT INTO `cadastro` VALUES (NULL,111111000,2),('silvio',1111110,3),('silvio',111111,4),('julia',1234570,5),('lyvia',1234570000,6),('lyvia',1234,7),('lyvia',1234,8),('lyvia',1234,9),('silvio',1234,10),('juliana',12345700,11),('bispo',123457000,12),('blblbl',19283500,13),('julisana',123476000,14),('qlwqdkj',8342750000,15),('qwmdme',10973800,16),('sdkxfklc',3407250,17),('jose',11128500,100),(NULL,NULL,600),('csk',184475000,601),('caio',184607000,602),('wesley',57970300,603),('kaique',284067000,604),('gregory',7683950000,605),('georgio ',239577000,606),('calabreso',4739290000,607),('vitoria',8475050000,608),('carlos',56385600,609),('maria',75867400,610),('cristiano',9488590000,611),('messi',848483000,612),('julio cesar',758373000000,613),('ederson',1847800000,614),('natan',59382900,615),('trigo',48429900000,616),('ferchat',2828280000,617),('carlito',8583740000,618),('richar',8757750000,619),('chet',484849000,620),('juio',24875600000,621),('caio c',28874900,622),('gio',283757000,623),('lau',381194000,624),('julio p',838384000,625),('galio',819376000,626),('helio',819286000,627),('gabi',738285000,628),('helen',847321000,629),('leo',847283000,630),('hyago',83758500,631),('dandan',48959800000,632),('caca',938746000,633),('melk',938279000,634),('bin',3835740,635),('sandra',164728000,636),('julio',73627600,637),('caio luccas',746285000,638),('faafa',387373000,639),('duduzinho',384758000,640),('zezinho',8753640,641),('jujuzinho',30394900,642),('cacu',3939860,643),('azzy',948557000,644),('gugu',857858000,645),('giova',38475700,646),('memem',294587000,647),('giorno',38485800,648),('jotaro',2975690,649),('yasm',945867,650),('gustavo',39588500,651),('juju',938848000,652);
/*!40000 ALTER TABLE `cadastro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `conta`
--

DROP TABLE IF EXISTS `conta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `conta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `saldo` float NOT NULL,
  `dtm` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_id` FOREIGN KEY (`id`) REFERENCES `cadastro` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=653 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conta`
--

LOCK TABLES `conta` WRITE;
/*!40000 ALTER TABLE `conta` DISABLE KEYS */;
INSERT INTO `conta` VALUES (11,3299,'2023-10-28 17:46:30'),(600,0,NULL),(601,0,NULL),(602,0,NULL),(613,0,NULL),(614,0,NULL),(615,0,NULL),(616,0,NULL),(617,0,NULL),(618,0,NULL),(619,0,NULL),(620,0,NULL),(621,0,NULL),(622,0,NULL),(623,0,NULL),(624,0,NULL),(625,0,NULL),(626,0,NULL),(627,0,NULL),(628,0,NULL),(629,0,NULL),(630,0,NULL),(631,0,NULL),(632,0,NULL),(633,701,'2023-10-19 15:51:46'),(634,0,'2023-10-19 16:40:44'),(635,214,'2023-10-19 17:54:10'),(636,-100,'2023-10-27 18:30:01'),(637,200,'2023-10-27 18:30:27'),(638,0,'2023-10-27 18:54:23'),(639,0,'2023-10-27 19:01:47'),(640,0,'2023-10-27 19:05:53'),(641,0,'2023-10-27 19:11:16'),(642,0,'2023-10-27 19:37:05'),(643,0,'2023-10-27 19:38:18'),(644,0,'2023-10-27 19:49:02'),(645,0,'2023-10-27 19:50:59'),(646,0,'2023-10-27 19:56:41'),(647,0,'2023-10-27 21:47:25'),(648,0,'2023-10-27 22:09:28'),(649,0,'2023-10-27 23:43:23'),(650,0,'2023-10-27 23:48:13'),(651,200,'2023-10-28 17:24:39'),(652,20,'2023-10-28 17:45:43');
/*!40000 ALTER TABLE `conta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'caixaecono'
--

--
-- Dumping routines for database 'caixaecono'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-28 20:00:29
