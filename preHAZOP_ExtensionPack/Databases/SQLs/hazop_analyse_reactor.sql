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
-- Table structure for table `reactor`
--

DROP TABLE IF EXISTS `reactor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reactor` (
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
  `Danger of leakage` varchar(255) DEFAULT NULL,
  `Dangerous level` varchar(255) DEFAULT NULL,
  `Safeguard_1` varchar(255) DEFAULT NULL,
  `Safeguard_2` varchar(255) DEFAULT NULL,
  `References` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reactor`
--

LOCK TABLES `reactor` WRITE;
/*!40000 ALTER TABLE `reactor` DISABLE KEYS */;
INSERT INTO `reactor` VALUES (20,'High pressure in reactor (general)','Higher','Pressure','uncontrolled reaction occurs','too much reactant into reactor','too littel product flow out of reactor','reactor material could weaken','causing leak or explosion','-',NULL,'Yes',NULL,'install high pressure alarm','install safety valve','Hazard and Operability Analysis of an Enthylene Oxide Production Plant'),(21,'Low pressure in reactor (general)','Lower','Pressure','too much product flow leaving the reactor','temperature dramatically decreases','-','uncontroll reactant and product flow into reactor','-','-',NULL,NULL,NULL,'install pressure sensor','add valve controls onto product and reactant lines','Hazard and Operability Analysis of an Enthylene Oxide Production Plant'),(22,'High temperature in reactor (general)','Higher','Temperature','incoming reactant temperature is too high','reaction thermodynamics proceed in an uncontrolled fashion','-','reactor could overheat','reactor pressure could increase','-',NULL,NULL,NULL,'install temperature sensor ','add thermal control jacket to reactor','Hazard and Operability Analysis of an Enthylene Oxide Production Plant'),(23,'Low temperature in reactor (general)','Lower','Temperature','incoming reactant temperature is too low','heat jacket to reactor out','-','reaction kinetics would be affected','reactor pressure could decrease','-',NULL,NULL,NULL,'install temperature sensor','add thermal control jacket to reactor','Hazard and Operability Analysis of an Enthylene Oxide Production Plant'),(24,'Low level in reactor (general)','Lower','Level','incorrect operation','low feed in reacor',NULL,'reduced amount of product ',NULL,NULL,NULL,NULL,NULL,'install remote valves on the feed','install low level alarm','Yang'),(25,'High level in reactor (general)','Higher','Level','incorrect operation','more feed in reactor','output valve incorrectly closed','high conversion in reactor','high temperature','-',NULL,NULL,NULL,'install remote valves on the feed','install high level alarm','Yang');
/*!40000 ALTER TABLE `reactor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-19 22:15:09
