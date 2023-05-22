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
-- Table structure for table `vessel`
--

DROP TABLE IF EXISTS `vessel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vessel` (
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
  `Substance` varchar(20) DEFAULT NULL,
  `Danger of leakage` varchar(20) DEFAULT NULL,
  `Dangerous level` varchar(20) DEFAULT NULL,
  `Safeguard_1` varchar(255) DEFAULT NULL,
  `Safeguard_2` varchar(255) DEFAULT NULL,
  `References` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vessel`
--

LOCK TABLES `vessel` WRITE;
/*!40000 ALTER TABLE `vessel` DISABLE KEYS */;
INSERT INTO `vessel` VALUES (26,'High pressure in vessel (general)','Higher','Pressure','high Temperatur','exothermic reaction in the vessel','-','risk of leakage','burst','-',NULL,'Yes',NULL,'install high pressure alarm','install safety valve','Kletz_what went wrong and Yang'),(27,'High level in vessel (general)','Higher','Level','human error','operation error','indicates the level in the vessel is almost twice the actual level.','overflow in the tank','risk of leakage','-',NULL,'Yes',NULL,'install high level alarm','installation of more than one measurement for the vessel','Kletz_what went wrong and Yang'),(28,'Low level in vessel (general)','Lower','Level','vessel defect','operation error',NULL,'risk of leakage','-','-',NULL,'Yes',NULL,'install low level alarm','-','Yang'),(29,'Low pressure in vessel (general)','Lower','Pressure','fire in the tank','the temperature in the vessel is too low','-','vessel defect','-','-',NULL,NULL,NULL,'install pressure sensor','-','Yang'),(30,'High temperature in vessel (general)','Higher','Temperature','high temperature of feeding','exothermic reaction in the vessel','-','risk of leakage','vessel defect','-',NULL,NULL,NULL,'install temperature sensor','install high temperature alarm','Yang'),(31,'Low temperature in vessel (general)','Lower','Temperature','evaporation of the stored chemicals','low temperature of the environment','-','risk of freezing','change of product quality','-',NULL,NULL,NULL,'install temperature sensor','install low temperature alarm','Yang'),(32,'More flow from outlet pipe into tank (general)','Reverse','Flow','operation error','lower pressure in vessel','-','risk of overflow in the tank','-',NULL,NULL,NULL,NULL,'install check valve on the outlet','-','Yang');
/*!40000 ALTER TABLE `vessel` ENABLE KEYS */;
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
