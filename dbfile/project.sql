/*
Navicat MySQL Data Transfer

Source Server         : qa.dangdang.com
Source Server Version : 50095
Source Host           : 10.255.254.129:3306
Source Database       : doc_master

Target Server Type    : MYSQL
Target Server Version : 50095
File Encoding         : 65001

Date: 2014-01-13 10:40:41
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for project
-- ----------------------------
DROP TABLE IF EXISTS `project`;
CREATE TABLE `project` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL,
  `create_date` datetime default NULL,
  `update_date` datetime default NULL,
  `user_id` int(11) default NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=104 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of project
-- ----------------------------
INSERT INTO `project` VALUES ('97', 'docMaster使用说明页', '2014-01-06 10:50:24', null, '100');
INSERT INTO `project` VALUES ('98', 'docMaster管理页', '2014-01-06 10:49:53', null, '100');
INSERT INTO `project` VALUES ('99', 'docMaster首页', '2013-12-26 16:00:19', null, '100');
INSERT INTO `project` VALUES ('100', 'DDAP项目文档', '2013-12-26 15:58:43', '2013-12-26 15:58:45', '100');
INSERT INTO `project` VALUES ('101', 'MData项目文档', '2014-01-06 18:26:04', null, null);
INSERT INTO `project` VALUES ('102', 'APIOW项目文档', '2014-01-06 18:31:48', null, null);
INSERT INTO `project` VALUES ('103', 'SendBox页面', '2014-01-07 18:54:51', '2014-01-09 17:09:02', null);
