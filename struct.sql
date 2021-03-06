/* 
  for dump.sql (include structure and data)
  download from: xxx
*/

/* recipes table */
DROP TABLE IF EXISTS `recipes`;
CREATE TABLE `recipes` (
  `name` mediumtext,
  `id` bigint(20) NOT NULL,
  `minutes` bigint(20) DEFAULT NULL,
  `contributor_id` bigint(20) DEFAULT NULL,
  `submitted` mediumtext,
  `tags` mediumtext,
  `nutrition` mediumtext,
  `n_steps` bigint(20) DEFAULT NULL,
  `steps` mediumtext,
  `description` mediumtext,
  `ingredients` mediumtext,
  `n_ingredients` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/* token table (api key) */
DROP TABLE IF EXISTS `apikey`;
CREATE TABLE `apikey` (
  `apikeyid` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) NOT NULL,
  `apikey` varchar(255) NOT NULL,
  `updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`apikeyid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/* user table */
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` varchar(255) NOT NULL,
  PRIMARY KEY (`userid`),
  UNIQUE (`username`),
  CONSTRAINT CHECK (`role` IN ('user','admin'))
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `apikey` ADD FOREIGN KEY (`userid`) REFERENCES `user`(`userid`);
