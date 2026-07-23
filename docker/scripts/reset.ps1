Set-Location "$PSScriptRoot\.."

docker compose `
    --env-file .env `
    -f compose/docker-compose.yml `
    down -v

docker volume prune -f