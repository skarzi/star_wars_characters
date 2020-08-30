#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset


###############################################################################
# Wait with timeout until PostgreSQL connected.
#
# Globals:
#   None
# Arguments:
#   $1 - PostgreSQL server host
#   $2 - PostgreSQL server port - default to `5432`
#   $3 - timeout - default `1 min`
#   $4 - retry interval - default `1s`
# Returns:
#   None
###############################################################################
wait_for_postgres() {
    local host="${1}"
    local port="${2:-5432}"
    local timeout="${3:-60s}"
    local retry_interval="${4:-1s}"

    dockerize \
        -wait "tcp://${host}:${port}" \
        -wait-retry-interval "${retry_interval}" \
        -timeout "${timeout}"
}


# Ensure postgresql is started and ready to accept connections within 60s
>&2 echo 'Waiting for PostgreSQL..'
wait_for_postgres "${POSTGRES_HOST}" "${POSTGRES_PORT}" "60s"
>&2 echo 'PostgreSQL is available'

exec "$@"
