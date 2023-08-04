SHELL := /bin/bash
CWD := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
ME := $(shell whoami)

nothing:
	@echo "do nothing"

up:
	docker-compose up --remove-orphans --build \
		data_aggregator__balancer \
		data_aggregator__api \
		data_aggregator__device__api \
		data_aggregator__db__ui \
		data_aggregator__web \
		data_aggregator__broker__amqp \
		data_aggregator__uni_worker__data_reception_input \
		data_agreggator__uni_worker__event \
		data_agreggator__uni_worker__device_data \

check_env:
	@./srv/check_env.sh

cleanup:
	docker login gitlab.neroelectronics.by:5050 -u unic_lab_developers -p Vw3o4gBzgH_GGUzFs7NM

	git submodule init
	git submodule update --remote

	pipenv sync --dev
	pipenv clean

	ulpytool install

lint:
	pipenv run lint

tests:
	pipenv run test

drop:
	docker-compose down -v

fix_own:
	@echo "me: $(ME)"
	sudo chown $(ME):$(ME) -R .

######################## MANAGER DEVICE DB START ########################

data_aggregator__db__migrations:
	docker-compose run --rm manager__data_aggregator__db /docker_app/src/data_aggregator__db/bin-migrate.sh --migrate

data_aggregator__db__revision:
	docker-compose run --rm manager__data_aggregator__db /docker_app/src/data_aggregator__db/bin-migrate.sh --revision

data_aggregator__db__init:
	docker-compose run --rm manager__data_aggregator__db /docker_app/src/data_aggregator__db/bin-migrate.sh --init

data_aggregator__db__upgrade:
	docker-compose run --rm manager__data_aggregator__db /docker_app/src/data_aggregator__db/bin-migrate.sh --upgrade

data_aggregator__db__downgrade:
	docker-compose run --rm manager__data_aggregator__db /docker_app/src/data_aggregator__db/bin-migrate.sh --downgrade

data_aggregator__db__import_mac:
	docker-compose run --rm manager__data_aggregator__db /docker_app/src/data_aggregator__db/bin-import-mac.sh

data_aggregator__db__generation_value:
	docker-compose run --rm manager__data_aggregator__db /docker_app/src/data_aggregator__db/bin-generation-values.sh

data_aggregator__db__upgrade_locals:
	SERVICE_DATA_AGGREGATOR_DB__DB_URI="postgresql://admin:admin@localhost:3332/device_db" SERVICE_DATA_AGGREGATOR_DB__SYS_USER_ID="6ff8eaba-b5b4-49b2-9a83-f48fcdf6d361" SERVICE_DATA_AGGREGATOR_DB__SYS__TYPE_ID="c8a0811f-24a8-4517-aab8-e227f2b35533" SERVICE_DATA_AGGREGATOR_DB__SYS__MANUFACTURER_ID="d02f5807-4545-40fd-9f5d-091822d6868f" SERVICE_DATA_AGGREGATOR_DB__SYS__GATEWAY_ID="e77ea8e3-105b-410d-b383-f0f6a62efca9" SERVICE_DATA_AGGREGATOR_DB__SYS__PROTOCOL_ID_SMP="f95ec7ef-07bb-4dac-aa26-8bca2e6cfc3b" SERVICE_DATA_AGGREGATOR_DB__SYS__PROTOCOL_ID_SMP_NCP="6e65e16c-38b1-430f-bb05-e28242af214a" SERVICE_DATA_AGGREGATOR_DB__SYS__PROTOCOL_ID_WATER_5="f2aee1b0-8d8f-4800-92bc-b60213cb0df7" SERVICE_DATA_AGGREGATOR_DB__SYS__GATEWAY_NETWORK_ID="324570cc-aef6-4a05-8989-ee246155bf7d" SERVICE_DATA_AGGREGATOR_DB__SYS__GATEWAY_NETWORK__SMP_UDP_SERVER__ID="3b0ab436-7357-4041-8533-0b48b41d097d" SERVICE_DATA_AGGREGATOR_DB__SYS__GATEWAY_NETWORK__SMP_NCP_UDP_SERVER__ID="c11e99b9-eaaa-4972-a34f-2303da768ac8" NERO_OLD__ENC_KEY_ID='032f7c78-a871-48ce-a0f3-8633152429a9' NERO_OLD__AES_KEY='SHH2sXqzQ9pAXmFj3S3aydbKwwqxdd6M' ./src/data_aggregator__db/bin-migrate.sh --upgrade

data_aggregator__db__archive:
	sh ./src/bin_archive.sh

data_aggregator__db__restore:
	sh ./src/bin_restore.sh
######################## MANAGER DEVICE DB END ########################
