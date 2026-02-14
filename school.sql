-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 24, 2024 at 03:56 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

/*SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";
*/

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
PRAGMA foreign_keys = ON;
--
-- Database: `school`
--

-- --------------------------------------------------------

--
-- Table structure for table `student_info`
--

CREATE TABLE `student_info` (
  `ENROLL_UID` int(11) NOT NULL PRIMARY KEY,
  `ENROLL_DATE` date DEFAULT NULL,
  `NAME` varchar(40) NOT NULL,
  `HOME_ADDRESS` varchar(100) DEFAULT '',
  `BIRTH_DATE` date DEFAULT NULL
) /*ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci*/;

-- ---------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `SRL_NMBR` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `ENROLL_UID` int(11) NOT NULL UNIQUE,
  `FIRST_NAME` varchar(40) NOT NULL,
  `LAST_NAME` varchar(40) DEFAULT '',
  `CLASS_ID` varchar(2) DEFAULT NULL CHECK (`CLASS_ID` in ('I','II','III','IV','V')),
  FOREIGN KEY(ENROLL_UID) REFERENCES student_info(ENROLL_UID)
) /*ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci*/;

-- --------------------------------------------------------
--
-- Table structure for table `class_i`
--


CREATE TABLE `class_i` (
  `ENROLL_UID` int(11) NOT NULL UNIQUE,
  `ENGLISH` decimal(3,2) DEFAULT NULL CHECK (`ENGLISH` <= 100),
  `SECLANG` decimal(3,2) DEFAULT NULL CHECK (`SECLANG` <= 100),
  `MATH` decimal(3,2) DEFAULT NULL CHECK (`MATH` <= 100),
  `DRAWING` decimal(3,2) DEFAULT NULL CHECK (`DRAWING` <= 100),
  `PET` decimal(3,2) DEFAULT NULL CHECK (`PET` <= 100),
  `GRADE` varchar(1) DEFAULT NULL CHECK (`GRADE` in ('S','A','B','C','D')),
  FOREIGN KEY(ENROLL_UID) REFERENCES students(ENROLL_UID)
) /*ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci*/;

-- --------------------------------------------------------

--
-- Table structure for table `class_ii`
--

CREATE TABLE `class_ii` (
  `ENROLL_UID` int(11) NOT NULL UNIQUE,
  `ENGLISH` decimal(3,2) DEFAULT NULL CHECK (`ENGLISH` <= 100),
  `SECLANG` decimal(3,2) DEFAULT NULL CHECK (`SECLANG` <= 100),
  `MATH` decimal(3,2) DEFAULT NULL CHECK (`MATH` <= 100),
  `EVS` decimal(3,2) DEFAULT NULL CHECK (`EVS` <= 100),
  `DRAWING` decimal(3,2) DEFAULT NULL CHECK (`DRAWING` <= 100),
  `PET` decimal(3,2) DEFAULT NULL CHECK (`PET` <= 100),
  `GRADE` varchar(1) DEFAULT NULL CHECK (`GRADE` in ('S','A','B','C','D')),
  FOREIGN KEY(ENROLL_UID) REFERENCES students(ENROLL_UID)
) /*ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci*/;

-- --------------------------------------------------------

--
-- Table structure for table `class_iii`
--

CREATE TABLE `class_iii` (
  `ENROLL_UID` int(11) NOT NULL UNIQUE,
  `ENGLISH` decimal(3,2) DEFAULT NULL CHECK (`ENGLISH` <= 100),
  `SECLANG` decimal(3,2) DEFAULT NULL CHECK (`SECLANG` <= 100),
  `MATH` decimal(3,2) DEFAULT NULL CHECK (`MATH` <= 100),
  `EVS` decimal(3,2) DEFAULT NULL CHECK (`EVS` <= 100),
  `DRAWING` decimal(3,2) DEFAULT NULL CHECK (`DRAWING` <= 100),
  `PET` decimal(3,2) DEFAULT NULL CHECK (`PET` <= 100),
  `GRADE` varchar(1) DEFAULT NULL CHECK (`GRADE` in ('S','A','B','C','D')),
  FOREIGN KEY(ENROLL_UID) REFERENCES students(ENROLL_UID)
) /*ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci*/;

-- --------------------------------------------------------

--
-- Table structure for table `class_iv`
--

CREATE TABLE `class_iv` (
  `ENROLL_UID` int(11) NOT NULL UNIQUE,
  `ENGLISH` decimal(3,2) DEFAULT NULL CHECK (`ENGLISH` <= 100),
  `SECLANG` decimal(3,2) DEFAULT NULL CHECK (`SECLANG` <= 100),
  `MATH` decimal(3,2) DEFAULT NULL CHECK (`MATH` <= 100),
  `SCIENCE` decimal(3,2) DEFAULT NULL CHECK (`SCIENCE` <= 100),
  `DRAWING` decimal(3,2) DEFAULT NULL CHECK (`DRAWING` <= 100),
  `PET` decimal(3,2) DEFAULT NULL CHECK (`PET` <= 100),
  `GRADE` varchar(1) DEFAULT NULL CHECK (`GRADE` in ('S','A','B','C','D')),
  FOREIGN KEY(ENROLL_UID) REFERENCES students(ENROLL_UID)
) /*ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci*/;

-- --------------------------------------------------------

--
-- Table structure for table `class_v`
--

CREATE TABLE `class_v` (
  `ENROLL_UID` int(11) NOT NULL UNIQUE,
  `ENGLISH` decimal(3,2) DEFAULT NULL CHECK (`ENGLISH` <= 100),
  `SECLANG` decimal(3,2) DEFAULT NULL CHECK (`SECLANG` <= 100),
  `MATH` decimal(3,2) DEFAULT NULL CHECK (`MATH` <= 100),
  `SCIENCE` decimal(3,2) DEFAULT NULL CHECK (`SCIENCE` <= 100),
  `DRAWING` decimal(3,2) DEFAULT NULL CHECK (`DRAWING` <= 100),
  `ECA` decimal(3,2) DEFAULT NULL CHECK (`ECA` <= 100),
  `PET` decimal(3,2) DEFAULT NULL CHECK (`PET` <= 100),
  `GRADE` varchar(1) DEFAULT NULL CHECK (`GRADE` in ('S','A','B','C','D')),
  FOREIGN KEY(ENROLL_UID) REFERENCES students(ENROLL_UID)
) /*ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci*/;

-- --------------------------------------------------------


--
-- Dumping data for table `student_info`
--

INSERT INTO `student_info` (`ENROLL_UID`, `ENROLL_DATE`, `NAME`, `HOME_ADDRESS`, `BIRTH_DATE`) VALUES
(1001, '2014-06-08', 'Raj Kiran', 'Salem TN', '2001-06-19'),
(1002, '2012-07-17', 'Sam Georgr', 'Erode TN', '2009-02-27');

INSERT INTO `students` (`ENROLL_UID`, `FIRST_NAME`, `LAST_NAME`, `CLASS_ID`) VALUES
(1001, 'Raj', 'Kiran','IV'),
(1002, 'Sam', 'Georgr', 'I');

INSERT INTO `class_i` (`ENROLL_UID`, `GRADE`) VALUES
(1002,'D');

INSERT INTO `class_iv` (`ENROLL_UID`, `GRADE`) VALUES
(1001,'D');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
