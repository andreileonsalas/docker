#!/bin/sh
set -e

get_ip() {
  ip a show dev eth0 | grep "inet " | cut -d' ' -f 6 | cut -d'/' -f 1
}

cd $DNDTOOLS_DIR/dndtools

if [ ! -f "dndproject/local.py" ]
then
  ln -s $DATA_DIR/local.py dndproject/local.py
fi


echo ========================================================
echo 
echo Starting dndtools on http://$(get_ip):8000
echo 
echo ========================================================
echo 
python manage.py help
python manage.py runserver $(get_ip):8000
echo server started at port 8000
