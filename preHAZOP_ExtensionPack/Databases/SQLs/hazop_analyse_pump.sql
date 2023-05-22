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
-- Table structure for table `pump`
--

DROP TABLE IF EXISTS `pump`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pump` (
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
-- Dumping data for table `pump`
--

LOCK TABLES `pump` WRITE;
/*!40000 ALTER TABLE `pump` DISABLE KEYS */;
INSERT INTO `pump` VALUES (1,'Failure of the seal (general)','Lower','Pressure','bearing failure','-','-','leak of chemicals','-','-',NULL,'Yes',NULL,'install pressure sensor','install check valve in the delivery line','Kletz_what went wrong'),(2,'Bearing failure (general)','Lower','Flow','lack of lubrication','-','-','failure of the seal','-','-',NULL,NULL,NULL,'install pressure sensor','install check valve in the delivery line','Kletz_what went wrong'),(3,'Pumping against wrongly closed valve results in damage of pump  (general)','Higher','Temperature','valve wrongly closed','-','-','damage to the seals','leak of chemicals','-',NULL,'Yes',NULL,'bypass','install remotely operated valves (controlled)','Holtermann_Masterarbeit'),(4,'Mechanical failure of the pump (general)','No','Flow','mechanical failure','power outage','-','damage','continuous process disturbed','-',NULL,NULL,NULL,'bypass','-','Holtermann_Masterarbeit with change from Yang'),(5,'Bursting of a pump (general)','Higher','Temperature','operating error, wrongly started between closed valves','pump housing made of brittle material','operating error went unnoticed','vapor pressure of the liquid raised','pump burst','-',NULL,'Yes',NULL,'install pressure sensor','install remotely operated valves (controlled)','DECHEMA Ereignis-Datenbank'),(6,'Centrifugal pump blast  (Pump, centrifugal type)','No','MSR','crystallization occurred and blockage of the pipeline over a longer period of time','failure of the volume flow monitoring system','no second measurement','reduction of volume flow','the organic liquid in the pipeline heated up until decomposed','the pump destroyed ',NULL,'Yes',NULL,'ensure the function of critical systems by second, independent measurement','install two or more MSR','DECHEMA Ereignis-Datenbank'),(7,'Failure in the cooling system  (general)','Lower','Temperature','low flow rates','failure in the cooling system (open more)','-','fat lose its viscosity','change of lubricant characteristic','damage to the bearings',NULL,NULL,NULL,'install temperature sensor','check the cooling system','www.researchgate.net/publication/291334094'),(8,'Pump damage due to high pressure (general)','Higher','Pressure','vaporizing liquid','blockage in the valve outlet','-','explosion','stop production',NULL,NULL,'Yes',NULL,'check and drain pipes and drain system','replace the gasket and check the damage','www.researchgate.net/publication/291334094'),(9,'Pump does not work  (general)','No','Pressure','pump failure','power outage','faulty pressure sensor','stop production','stop the pump','-',NULL,NULL,NULL,'check the types of liquids that can be used with the pump','install pressure sensor','www.researchgate.net/publication/291334094, Yang'),(10,'high flow rate in the pump (general)','Higher','Flow','blockage in the valve outlet','operating fault','too high engine power','overheating of the pump','destruction of the internal pump','cavitation',NULL,NULL,NULL,'install remotely operated valves (controlled)','check density of liquid that differens from the nominal density','www.researchgate.net/publication/291334094'),(11,'Idling of the centrifugal pump (Pump, centrifugal type)','No','Flow','closed discharge valve','inlet medium of the pump is not sufficient','-','overheating of the pump','mechanical damage','cavitation',NULL,NULL,NULL,'set up ldling sensing system','install flow sensor','https://angroupcn.com/learn-about-centrifugal-water-pump-idling/, s.o.');
/*!40000 ALTER TABLE `pump` ENABLE KEYS */;
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
