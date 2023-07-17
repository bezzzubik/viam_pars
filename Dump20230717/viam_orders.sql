-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: viam
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `work_type` varchar(45) DEFAULT NULL,
  `theme_contract` varchar(45) DEFAULT NULL,
  `transfer_act` varchar(45) DEFAULT NULL,
  `m_k` varchar(45) DEFAULT NULL,
  `customer` int NOT NULL,
  `plan_count_sample` int DEFAULT NULL,
  `fact_count_sample` int DEFAULT NULL,
  `kind_test` int DEFAULT NULL,
  `temperature` float DEFAULT NULL,
  `material` varchar(45) DEFAULT NULL,
  `tester` int NOT NULL,
  `count_tested_sample` int DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  `status_date` date DEFAULT NULL,
  `report_date` date DEFAULT NULL,
  `receive_sample_date_plan` date DEFAULT NULL,
  `receive_sample_date_fact` date DEFAULT NULL,
  `tester_receive_sample_date` date DEFAULT NULL,
  `test_end_date` date DEFAULT NULL,
  `protocol` varchar(45) DEFAULT NULL,
  `intensity_plan` float DEFAULT NULL,
  `intensity_fact` float DEFAULT NULL,
  `machine_list` int NOT NULL,
  `comment` varchar(45) DEFAULT NULL,
  `granta_mi_flag` int DEFAULT NULL,
  `granta_mi_text` varchar(45) DEFAULT NULL,
  `example_list` int NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `customer_idx` (`customer`),
  KEY `type_test_idx` (`kind_test`),
  KEY `tester_idx` (`tester`),
  KEY `machine_list_idx` (`machine_list`),
  KEY `example_list_idx` (`example_list`),
  CONSTRAINT `customer` FOREIGN KEY (`customer`) REFERENCES `customer` (`cust_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `example_list` FOREIGN KEY (`example_list`) REFERENCES `example_list` (`elist_id`),
  CONSTRAINT `machine_list` FOREIGN KEY (`machine_list`) REFERENCES `machine_list` (`list_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `tester` FOREIGN KEY (`tester`) REFERENCES `staff` (`staff_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `type_test` FOREIGN KEY (`kind_test`) REFERENCES `tests_types` (`type_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-17 16:49:47
