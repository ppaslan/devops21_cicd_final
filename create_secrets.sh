#!/usr/bin/env bash
set -e

help_menu() {
cat << EOF
Usage: $0 -n instance-name  registry-server -u registry-user -t registry-token -e registry-email [--help]

Required arguments:
-n                         App instance name
-s                         Container registry server
-u                         Registry user
-t                         Registry token
-e                         Registry email

Optional arguments
--help                   Prints this help text.
EOF
}

if [ "$1" == "--help" ]
then
    help_menu
    exit 0
fi

while getopts "n:s:u:t:e:" opt; do
  case $opt in
     n)
       release_name=$OPTARG
       ;;
     s)
       registry_server=$OPTARG
       ;;
     u)
       registry_user=$OPTARG
       ;;
     t)
       registry_token=$OPTARG
       ;;
     e)
       registry_email=$OPTARG
       ;;
     *)
       echo "Invalid arguments, for more info run $0 --help"
       exit 1
       ;;
  esac
done

required_args=($release_name $registry_server $registry_user $registry_token $registry_email)
mysql_secret_name="$release_name"-mysql-secret
shopapp_db_secret_name="$release_name"-secret
root_password=$(openssl rand -hex 18)
replication_password=$(openssl rand -hex 18)
user_password=$(openssl rand -hex 12)


if [[ "${#required_args[@]}" -ne 5 ]]
then
  echo "You're missing required arguments, for more info run $0 --help"
  exit 1
fi

kubectl create namespace "${release_name}" \
  --dry-run=client -o yaml \
  | kubectl apply -f -

kubectl create secret generic "$shopapp_db_secret_name" \
  -n "$release_name" \
  --from-literal=MYSQL_PASSWORD="$user_password" \
  -o yaml --dry-run=client | kubectl apply -f -

kubectl create secret generic "$mysql_secret_name" \
-n "$release_name" \
--from-literal=mysql-root-password="$root_password" \
--from-literal=mysql-replication-password="$replication_password" \
--from-literal=mysql-password="$user_password" \
-o yaml --dry-run=client | kubectl apply -f -

kubectl create secret docker-registry regcred \
  -n "$release_name" \
  --docker-server=$registry_server \
  --docker-username=$registry_user \
  --docker-password=$registry_token \
  --docker-email=$registry_email \
  -o yaml --dry-run=client | kubectl apply -f -
