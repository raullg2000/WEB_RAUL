-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 01-03-2026 a las 16:08:33
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `web_raul`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `posts`
--

CREATE TABLE `posts` (
  `id` int(11) NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `contenido` text NOT NULL,
  `autor_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `posts`
--

INSERT INTO `posts` (`id`, `titulo`, `contenido`, `autor_id`) VALUES
(1, 'Kill Bill', 'Imprescindible\r\n', 1),
(2, 'Star Wars', 'Me encanta Han Solo\r\n', 2),
(3, 'Terminator', 'Que bien lo hace el Suasenaguer\r\n', 7),
(4, 'Karate Kid', 'Que grande el señor Miyagi', 3),
(5, 'Pulp Fiction', 'Que guapa sale la Uma Thurman', 5),
(6, 'Jurasic Park', 'Que miedo pase en la parte de los Velociraptors :0', 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `resenas`
--

CREATE TABLE `resenas` (
  `id` int(11) NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `contenido` text NOT NULL,
  `username` varchar(100) NOT NULL,
  `fecha` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `username`, `password`) VALUES
(1, 'raul_test', 'scrypt:32768:8:1$4IEjFUFSNiQBGgze$6a9c46c7a817847abe49f9bc3d0bba67c23bd4e44dbb3a0520357a909d6cca0bbe8b2327e295907affb35bfa67bc68bb8f2a877249fcc6c20e91ebecd8aaed65'),
(2, 'patata', 'scrypt:32768:8:1$MPQxPFnZ4QMGlp4j$778dce13f86faddffb7570282b070354972454b3953729c34592368ab8279541ca05f48dccfeba9bd4a1f516baf762132247198f15a5bda05ca2db3e8812b63b'),
(3, 'joel', 'scrypt:32768:8:1$4hkl3CF7NEqYKMtL$b94adfd8ab1912d4c403721665a4ab09d138eac4b4888e35382355dedc9a35ee1bad621413894e6784570e8909dccdfbe85858611a180275472dc754fc26ad21'),
(4, 'fredy', 'scrypt:32768:8:1$m2kiB6SSLixC8tpA$c09f3886291464ddaa51e01a5d4c09b7e209a362122ef6ff05d6e212850bb072da6d8d81fcbb2496804d98da2804d0f0d64a4e6fa7f781739a4bc7fb7a967a6f'),
(5, 'myrna', 'scrypt:32768:8:1$TdgI2AFFEMVJlCZ6$9d625d9e0d84825df67347352b227bf3ed5af688a83acc2b32c81797eb13f86c89f56a2a9994128c34a658ba94338730294466dc29309d64f8caa64388b2aebe'),
(6, 'edgar', 'scrypt:32768:8:1$1mIjTk5YEtZFF9s0$9b3e1292d0e4b029d8955d927ee5eac3279b4c3d20539f1ee0cc321a563aaeeb89904993dde9596c1fb724c806d84dd1acdb157a0a8395bcfca395d114d10b63'),
(7, 'mercedes', 'scrypt:32768:8:1$JCYZ1TkSXtgqYqFz$6b0ffd0da068c510aa3199cb65966b8d297ba7cfa31c08acba17037f44a38ba24c33b5285a151038b451aacda841b917f82953d38e88e985861497f7ebbae793');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`id`),
  ADD KEY `autor_id` (`autor_id`);

--
-- Indices de la tabla `resenas`
--
ALTER TABLE `resenas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `posts`
--
ALTER TABLE `posts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `resenas`
--
ALTER TABLE `resenas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `posts`
--
ALTER TABLE `posts`
  ADD CONSTRAINT `posts_ibfk_1` FOREIGN KEY (`autor_id`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
