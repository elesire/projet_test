DROP TABLE IF EXISTS `blog_billet`;
CREATE TABLE `blog_billet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `photo` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `blog_billet` (`id`, `name`, `description`, `photo`) VALUES
(1,	'manzhouli',	'bmn q< jnmbo n< nù nire thno n htno nb  nbhno',	'photos/DSC02979.JPG');