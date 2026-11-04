<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the website, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://developer.wordpress.org/advanced-administration/wordpress/wp-config/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'cc' );
define('WP_ALLOW_REPAIR', true);
/** Database username */
define( 'DB_USER', 'root' );

/** Database password */
define( 'DB_PASSWORD', '' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'D;]I&dgq<.-FV{Tqo|g@T*fV8Ksnc3]7na~`)o*#|01$52WK-X.n%Ro:9=pU5c-0' );
define( 'SECURE_AUTH_KEY',  '6I{U]5n`Jzh?2R>$;X]s*dM.a2Wzd8BT.-iuX XS%R51-S:zJQZkt5NHlWiPOK$)' );
define( 'LOGGED_IN_KEY',    'fFo zPD~$7H}<{g*3RoCer! Z<]]!d<!y]AY:l(mEKcN#z0R!@rz9OY QL6_H$7/' );
define( 'NONCE_KEY',        '?Hh Av~rX,.W9F{{])/Z[N$@aivYNhG2+dhI-4B-q4>3(Pf&H61RqI0i|Pm%rh{<' );
define( 'AUTH_SALT',        'xTD${Adl_X{o!6?tEUC{#soRV5?<tA1*pEoy=w}x)Uo1!iRcFWNQ_p%.#[-8i]O@' );
define( 'SECURE_AUTH_SALT', 'LF8McP[2U?]J,7l.KpIMc*=4o]u/RAN{V!4W(3di-vsAcTtP=]QXGVh~h<f<@|Pp' );
define( 'LOGGED_IN_SALT',   '9w(|N(RO$SZyIlL55CWf>,[CO>G}ACYhb}wu+Q<p,q^G4W%f00dt^~62~xfT^__X' );
define( 'NONCE_SALT',       'aRVD5;=igRsP}[+a;}f9SUC1jkfN/+R45Z=!ryQVt9C^;9W3r;jX}$)xun<8@!W=' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 *
 * At the installation time, database tables are created with the specified prefix.
 * Changing this value after WordPress is installed will make your site think
 * it has not been installed.
 *
 * @link https://developer.wordpress.org/advanced-administration/wordpress/wp-config/#table-prefix
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://developer.wordpress.org/advanced-administration/debug/debug-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
