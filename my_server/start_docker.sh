if docker images | grep -q "my_server_image"; then
    echo "Image exists"
else
    docker build -t my_server_image .
fi

docker run -it -d -p 5000:5000/tcp --name my_server -v .:/app my_server_image python3 /app/server_side.py