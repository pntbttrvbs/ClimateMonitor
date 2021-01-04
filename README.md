# ClimateMonitor

This is a small Raspberry Pi based project to track the temperature and humidity in certain parts of my house so I can look at insulation requirements. 


## Dependencies

flask should be installed with most python3 distros

<pre><code>
$ sudo pip3 install adafruit-circuitpython-dht
$ sudo apt-get install libgpiod2
$ sudo
</pre></code>

## Set up database

<pre><code>
sudo mysql
create user pi IDENTIFIED by 'raspberry';
grant all privileges on *.* to 'pi' with grant option;
create database climate;
use climate;
CREATE TABLE CLIMATE_MEASUREMENT( 
ID BIGINT NOT NULL AUTO_INCREMENT,
REMOTE_ID BIGINT;
AMBIENT_TEMPERATURE_CELCIUS TINYINT NOT NULL,
HUMIDITY TINYINT NOT NULL,
CREATED TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
PRIMARY KEY ( ID )
);
