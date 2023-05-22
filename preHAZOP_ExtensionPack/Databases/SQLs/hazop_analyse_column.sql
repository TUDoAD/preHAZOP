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
-- Table structure for table `column`
--

DROP TABLE IF EXISTS `column`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `column` (
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
-- Dumping data for table `column`
--

LOCK TABLES `column` WRITE;
/*!40000 ALTER TABLE `column` DISABLE KEYS */;
INSERT INTO `column` VALUES (33,'Low temperature in the column (general)','Lower','Temperature','low environmental temperature','lower feed temperature','-','low purity of product','-','-',NULL,NULL,NULL,'install low temperature alarm','-','Yang'),(34,'High pressure in the column  (general)','Higher','Pressure','too long residence time due to operational disturbances','occurrence of an autocatalytic decomposition process','thermally unstable component being constricted too much','decomposition of substances','unexpected rise in temperature and presure','-',NULL,NULL,NULL,'install safety valve ','install high pressure alarm','DECHEMA Ereignis-Datenbank'),(35,'High temperature in the column (general)','Higer','Temperature','too long residence time due to operational disturbances','occurrence of an autocatalytic decomposition process','thermally unstable component being constricted too much','decomposition of substances','unexpected rise in temperature and presure','-',NULL,NULL,NULL,'DTA measurements of the input mixture and the concentrated residue and the distillate','install high temperature alarm','DECHEMA Ereignis-Datenbank'),(36,'Substance leakage due to corrosion of a weld seam (general)','Lower','Pressure','a high flow velocity in the area of the weld seam attacked the seam mechanically and chemical corrosion','-','-','leaks occurred in the area of the column sump','leak of product','-',NULL,'Yes',NULL,'avoid weld seams in general if possible','reduce the flow velocity in the area of weld seams','DECHEMA Ereignis-Datenbank + Yang'),(37,'No flow in the column (general)','No','Flow','feed pump defective','low level alarm and control valve shut','tube leakages and blocking','column dry out','no operation','-',NULL,NULL,NULL,'bypass','install low level alarm','www.academia.edu/33328920/HAZOP_for_Distillation_column_Parameter_Guideword_Deviation_Possible_Cause_Consequence_Action_Flow_NO_No_flow_at_BULLET_Pipe_blockages'),(38,'Less flow in the column (general)','Low','Level','pipe blockages','low level alarm control valve shut','tube leakages and blocking','changes in product quality','possible dangerous concentration','',NULL,NULL,NULL,'bypass','install low level alarm','www.academia.edu/33328920/HAZOP_for_Distillation_column_Parameter_Guideword_Deviation_Possible_Cause_Consequence_Action_Flow_NO_No_flow_at_BULLET_Pipe_blockages'),(39,'More flow in the column (general)','High','Level','control valve failure','increase pumping capacity','low level alarm faulty','flooding in the column','changes in product quality','increased corrosion and fouling of downstream equipment',NULL,NULL,NULL,'install high level alarm','install two independent control','www.academia.edu/33328920/HAZOP_for_Distillation_column_Parameter_Guideword_Deviation_Possible_Cause_Consequence_Action_Flow_NO_No_flow_at_BULLET_Pipe_blockages'),(40,'High relux flow in the distillation column (Column with bubble cap trays)','Higher','Flow','reflux control error ','distillate valve incorrectly closed, distillate valve opening smaller','feed stream too high','rain in the column (Durchregnen)','entrainment of liquid by steam flow','-',NULL,NULL,NULL,'independent reflux and distillate stream control','install feed flow control','Vorlesung_Prozessautomatisierung, Yang'),(41,'Low reflux flow in the distillation column (Column with bubble cap trays)','Lower','Flow','lower feed stream','lower condenser efficiency','-','entrainment of liquid by steam flow','low purity of product','-',NULL,NULL,NULL,'install flow rate control','check condenser','Vorlesung_Prozessautomatisierung, Yang'),(42,'No reflux flow in the distillation column (Column with bubble cap trays)','No','Flow','heat exchanger for condensation not in operation ','reflux flow control valve incorrectly closed','no feed flow in the distillation column','stop production','idling risk of the pump','-',NULL,NULL,NULL,'check heat exchanger for condensation regularly','check feed flow','Yang'),(43,'Feed temperature too low (Column with bubble cap trays)','Lower','Temperature','wrong operation ','-','-','low purity of product','-','-',NULL,NULL,NULL,'install temperature sensor for feed','-','Yang'),(44,'Feed temperature too high (Column with bubble cap trays)','Higher','Temperature','wrong operation ','-','-','loss of light component','high pressure in the column','-',NULL,NULL,NULL,'install temperature sensor for feed','-','Yang'),(45,'More feed to the distillation column (Column with bubble cap trays)','Higher','Flow','human error ','wrong operation','-','overflow in the column','risk of leakage','-',NULL,NULL,NULL,'install operation valve for feed','-','Yang'),(46,'Low feed to the  distillation column (Column with bubble cap trays)','Lower','Flow','wrong operation ','feed pipe defect','feed blockage','risk of leakage','-','-',NULL,NULL,NULL,'install operation valve for feed','-','Yang');
/*!40000 ALTER TABLE `column` ENABLE KEYS */;
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
