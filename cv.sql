-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 16, 2023 at 03:20 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.3.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cv`
--

-- --------------------------------------------------------

--
-- Table structure for table `applicants`
--

CREATE TABLE `applicants` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(100) NOT NULL,
  `job_desc` text NOT NULL,
  `age` tinyint(3) UNSIGNED NOT NULL,
  `address` varchar(100) NOT NULL,
  `gender` enum('Male','Female','','') NOT NULL,
  `primary_role` enum('0','1','2','3') NOT NULL COMMENT '0: Web development, 1: Mobile development, 2: UI/UX, 3: DevOps',
  `primary_role_score` float UNSIGNED NOT NULL,
  `score` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`score`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `applicants`
--

INSERT INTO `applicants` (`id`, `name`, `job_desc`, `age`, `address`, `gender`, `primary_role`, `primary_role_score`, `score`) VALUES
(2, 'Fark', 'I love android', 12, 'Jalan Raya Pakisan', 'Male', '1', 0.548, '[0.189, 0.548, 0.182, 0.081]'),
(3, 'Fark2', 'I love android and kotlin', 13, 'Jalan bws', 'Male', '1', 0.694, '[0.077, 0.694, 0.072, 0.157]'),
(4, 'Fark3', 'I like to roll with github and kotlin, primarily, I\'m a developer with a high knowledge of mobile programming', 34, 'test3', 'Male', '1', 0.881, '[0.06, 0.881, 0.037, 0.022]');

-- --------------------------------------------------------

--
-- Table structure for table `jobs`
--

CREATE TABLE `jobs` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `description` text NOT NULL,
  `role` enum('0','1','2','3') NOT NULL COMMENT '0: Web development, 1: Mobile development, 2: UI/UX, 3: DevOps'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `jobs`
--

INSERT INTO `jobs` (`id`, `description`, `role`) VALUES
(1, 'Designnnnn, develop and improve high quality backend services, APIs and security, Develop and maintain integration to third party APIs', '0'),
(2, 'Design android apps with github and kotlinnn', '1'),
(3, 'Design a webpage / mobile using Figma and Adobe', '2'),
(4, 'Deploy infrastructure to AWS or GCP', '3');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `applicants`
--
ALTER TABLE `applicants`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `jobs`
--
ALTER TABLE `jobs`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `applicants`
--
ALTER TABLE `applicants`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `jobs`
--
ALTER TABLE `jobs`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
