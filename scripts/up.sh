docker compose -f services/kafka_service/docker-compose.yml up -d
docker compose -f services/order_service/docker-compose.yml up -d
docker compose -f services/user_service/docker-compose.yml up -d
docker compose -f services/product_service/docker-compose.yml up -d
docker compose -f services/review_service/docker-compose.yml up -d
