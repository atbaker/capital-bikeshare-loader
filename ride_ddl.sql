CREATE TABLE `ride` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `duration` int(11) NOT NULL,
  `start_date` datetime NOT NULL,
  `start_station` varchar(255) NOT NULL,
  `start_terminal` int(11) NOT NULL,
  `end_date` datetime DEFAULT NULL,
  `end_station` varchar(255) DEFAULT NULL,
  `end_terminal` int(11) DEFAULT NULL,
  `bike_number` varchar(45) NOT NULL,
  `subscription_type` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `BIKE_NUMBER` (`bike_number`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
