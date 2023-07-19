-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.10.2-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Volcando estructura para tabla hospedaje.habitacion

CREATE DATABASE hospedaje;
USE hospedaje;

CREATE TABLE IF NOT EXISTS `habitacion` (
  `cod_hab` varchar(4) NOT NULL COMMENT 'Código de la habitación',
  `num_hab` varchar(4) NOT NULL COMMENT 'Número de la habitación',
  `tip_hab` char(1) NOT NULL DEFAULT 'N' COMMENT 'Tipo de habitación (N normal, E ejecutiva, S suite)',
  `cap_hab` char(1) NOT NULL DEFAULT 'I' COMMENT 'Capacidad de la habitación (I individual, M matrimonial, D doble, T triple)',
  `pre_hab` decimal(12,2) NOT NULL DEFAULT 0.00 COMMENT 'Precio de la habitación',
  `sta_hab` char(1) NOT NULL DEFAULT 'D' COMMENT 'Status de la habitación (O ocupada, D desocupada)',
  PRIMARY KEY (`cod_hab`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci COMMENT='Tabla que almacena la información de las habitaciones';

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla hospedaje.huesped
CREATE TABLE IF NOT EXISTS `huesped` (
  `ced_hue` int(10) unsigned NOT NULL COMMENT 'Cédula del huésped',
  `ape_hue` varchar(50) NOT NULL COMMENT 'Apellidos del huésped',
  `nom_hue` varchar(50) NOT NULL COMMENT 'Nombres del huésped',
  `dir_hue` varchar(100) NOT NULL COMMENT 'Dirección del huésped',
  `ciu_hue` varchar(30) NOT NULL COMMENT 'Ciudad del huésped',
  `email_hue` varchar(70) NOT NULL COMMENT 'Email del huésped',
  `tel_hue` varchar(12) NOT NULL COMMENT 'Teléfono del huésped',
  PRIMARY KEY (`ced_hue`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci COMMENT='Tabla que guarda información de los huéspedes del hotel';

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla hospedaje.ingreso
CREATE TABLE IF NOT EXISTS `ingreso` (
  `cod_ing` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Código de ingreso',
  `ced_hue` int(10) unsigned NOT NULL COMMENT 'Cédula del huésped',
  `cod_hab` varchar(4) NOT NULL COMMENT 'Código de habitación del huésped',
  `fec_ing` datetime NOT NULL DEFAULT current_timestamp() COMMENT 'Fecha de ingreso del huésped',
  `fec_sal` datetime NOT NULL COMMENT 'Fecha de salida del huésped',
  `can_per` tinyint(3) unsigned NOT NULL DEFAULT 1 COMMENT 'Cantidad de personas que ocupan la habitación',
  PRIMARY KEY (`cod_ing`),
  KEY `FK_huesped` (`ced_hue`),
  KEY `FK_habitacion` (`cod_hab`),
  CONSTRAINT `FK_habitacion` FOREIGN KEY (`cod_hab`) REFERENCES `habitacion` (`cod_hab`) ON UPDATE CASCADE,
  CONSTRAINT `FK_huesped` FOREIGN KEY (`ced_hue`) REFERENCES `huesped` (`ced_hue`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci COMMENT='Tabla que registra los ingresos de los huéspedes en el hotel';

-- La exportación de datos fue deseleccionada.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;