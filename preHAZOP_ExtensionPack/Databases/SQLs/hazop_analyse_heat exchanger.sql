-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: hazop_analyse
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `heat exchanger`
--

DROP TABLE IF EXISTS `heat exchanger`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `heat exchanger` (
  `Index` int NOT NULL,
  `Description` varchar(255) DEFAULT NULL,
  `Guideword` varchar(255) DEFAULT NULL,
  `Parameter` varchar(255) DEFAULT NULL,
  `Cause_1` varchar(255) DEFAULT NULL,
  `Cause_2` varchar(255) DEFAULT NULL,
  `Cause_3` varchar(255) DEFAULT NULL,
  `Consequence_1` varchar(255) DEFAULT NULL,
  `Consequence_2` varchar(255) DEFAULT NULL,
  `Consequence_3` varchar(255) DEFAULT NULL,
  `Substance` varchar(255) DEFAULT NULL,
  `Danger of leakage` varchar(20) DEFAULT NULL,
  `Dangerous level` varchar(20) DEFAULT NULL,
  `Safeguard_1` varchar(255) DEFAULT NULL,
  `Safeguard_2` varchar(255) DEFAULT NULL,
  `References` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `heat exchanger`
--

LOCK TABLES `heat exchanger` WRITE;
/*!40000 ALTER TABLE `heat exchanger` DISABLE KEYS */;
INSERT INTO `heat exchanger` VALUES (12,'Reduced flow of heating or cooling medium (general)','Lower','Flow','pipe blockage','wrong operation','-','temperature of process fluid remains constant','-','-',NULL,'Yes',NULL,'install flow alarm ','-','https://www.ehsdb.com/hazop.php'),(13,'More cooling flow or heating flow (general)','More','Flow','failure of cooling flow valve or heating flow valve','wrong operation','-','temperature of process fluid decrease','-','-',NULL,NULL,NULL,'install flow alarm ','-','https://www.ehsdb.com/hazop.php'),(14,'More pressure on tube side of Shell&Tube Heat Exchanger (Heat exchanger with straight tubes)','Higher','Pressure','failure of process fluid valve','-','-','bursting of tube','-','-',NULL,'Yes',NULL,'Install high pressure alarm','-','https://www.ehsdb.com/hazop.php'),(15,'Contamination of process fluid line (general)','Lower','Pressure','leakage of tube and cooling flow or heating flow goes in','-','-','contamination of process fluid','-','-',NULL,'Yes',NULL,'proper maintainance and operator alert','-','https://www.ehsdb.com/hazop.php and Yang'),(16,'Corrosion of tube (Heat exchanger with straight tubes)','Corrosion','Tube','hardness of cooling water','-','-','less cooling and crack of tube','-','-',NULL,'Yes',NULL,'proper maintainence','-','https://www.ehsdb.com/hazop.php'),(17,'Reverse process fluid flow (general)','Reverse','Process fluid flow','failure of process fluid inlet valve','-','-','product off set','temperature of process fluid remains constant','-',NULL,NULL,NULL,'install check valve','-','https://www.ehsdb.com/hazop.php'),(18,'Restarting the heat exchangerl cause brittle failure (general)','Lower','Temperature','ice formed on the outside of the heat exchanger when the flow of warm heating medium  stopped','heat exchanger could not withstand low temperatures and thermal shocks','not clear in the operating instructions','the heat exchanger fractured','explosion because of releasing hydrocarbon vapors and liquids','-',NULL,'Yes',NULL,'the operators need to be good trained','install low temperature alarm','Kletz_what went wrong'),(19,'Pressure shock causes leakage at plate heat exchanger (plate heat exchanger)','Lower','Pressure','a pressure surge on the product side of the plate heat exchangers','-','-','seal failure','-','-',NULL,NULL,NULL,'sealing materials must be resistant','use shell and tube heat exchanger','DECHEMA Ereignis-Datenbank');
/*!40000 ALTER TABLE `heat exchanger` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-19 22:15:08
