# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from steel import Steel, AsyncSteel
from steel.types import (
    Environment,
    EnvironmentList,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnvironments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Steel) -> None:
        environment = client.environments.create(
            name="x",
        )
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Steel) -> None:
        environment = client.environments.create(
            name="x",
            network_secrets=[
                {
                    "domain": "domain",
                    "header": "header",
                    "secret": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "template": "{{secret}}",
                    "port": 1,
                }
            ],
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secrets={"foo": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
            spec={
                "auto_pause": True,
                "disk_mib": 1,
                "env": {"foo": "string"},
                "memory_mib": 128,
                "name": "x",
                "network_policy": {
                    "cidrs": {
                        "allow": ["x"],
                        "deny": ["x"],
                    },
                    "domains": {
                        "allow": ["x"],
                        "deny": ["x"],
                    },
                    "internet_access": True,
                },
                "template": "x",
                "timeout_seconds": 1,
                "vcpu": 1,
            },
        )
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Steel) -> None:
        response = client.environments.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Steel) -> None:
        with client.environments.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(Environment, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Steel) -> None:
        environment = client.environments.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Steel) -> None:
        environment = client.environments.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Steel) -> None:
        response = client.environments.with_raw_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Steel) -> None:
        with client.environments.with_streaming_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(Environment, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.environments.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update_overload_1(self, client: Steel) -> None:
        environment = client.environments.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        )
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Steel) -> None:
        environment = client.environments.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            network_secrets=[
                {
                    "domain": "domain",
                    "header": "header",
                    "secret": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "template": "{{secret}}",
                    "port": 1,
                }
            ],
            secrets={"foo": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
            spec={
                "auto_pause": True,
                "disk_mib": 1,
                "env": {"foo": "string"},
                "memory_mib": 128,
                "name": "x",
                "network_policy": {
                    "cidrs": {
                        "allow": ["x"],
                        "deny": ["x"],
                    },
                    "domains": {
                        "allow": ["x"],
                        "deny": ["x"],
                    },
                    "internet_access": True,
                },
                "template": "x",
                "timeout_seconds": 1,
                "vcpu": 1,
            },
        )
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    def test_raw_response_update_overload_1(self, client: Steel) -> None:
        response = client.environments.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_1(self, client: Steel) -> None:
        with client.environments.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(Environment, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_1(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.environments.with_raw_response.update(
                id="",
                name="x",
            )

    @parametrize
    def test_method_update_overload_2(self, client: Steel) -> None:
        environment = client.environments.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            spec={},
        )
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Steel) -> None:
        environment = client.environments.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            spec={
                "auto_pause": True,
                "disk_mib": 1,
                "env": {"foo": "string"},
                "memory_mib": 128,
                "name": "x",
                "network_policy": {
                    "cidrs": {
                        "allow": ["x"],
                        "deny": ["x"],
                    },
                    "domains": {
                        "allow": ["x"],
                        "deny": ["x"],
                    },
                    "internet_access": True,
                },
                "template": "x",
                "timeout_seconds": 1,
                "vcpu": 1,
            },
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
            network_secrets=[
                {
                    "domain": "domain",
                    "header": "header",
                    "secret": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "template": "{{secret}}",
                    "port": 1,
                }
            ],
            secrets={"foo": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
        )
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    def test_raw_response_update_overload_2(self, client: Steel) -> None:
        response = client.environments.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            spec={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_2(self, client: Steel) -> None:
        with client.environments.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            spec={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(Environment, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_2(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.environments.with_raw_response.update(
                id="",
                spec={},
            )

    @parametrize
    def test_method_update_overload_3(self, client: Steel) -> None:
        environment = client.environments.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secrets={"foo": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
        )
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_3(self, client: Steel) -> None:
        environment = client.environments.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secrets={"foo": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
            network_secrets=[
                {
                    "domain": "domain",
                    "header": "header",
                    "secret": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "template": "{{secret}}",
                    "port": 1,
                }
            ],
            spec={
                "auto_pause": True,
                "disk_mib": 1,
                "env": {"foo": "string"},
                "memory_mib": 128,
                "name": "x",
                "network_policy": {
                    "cidrs": {
                        "allow": ["x"],
                        "deny": ["x"],
                    },
                    "domains": {
                        "allow": ["x"],
                        "deny": ["x"],
                    },
                    "internet_access": True,
                },
                "template": "x",
                "timeout_seconds": 1,
                "vcpu": 1,
            },
        )
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    def test_raw_response_update_overload_3(self, client: Steel) -> None:
        response = client.environments.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secrets={"foo": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_3(self, client: Steel) -> None:
        with client.environments.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secrets={"foo": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(Environment, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_3(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.environments.with_raw_response.update(
                id="",
                secrets={"foo": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
            )

    @parametrize
    def test_method_update_overload_4(self, client: Steel) -> None:
        environment = client.environments.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            network_secrets=[
                {
                    "domain": "domain",
                    "header": "header",
                    "secret": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "template": "{{secret}}",
                }
            ],
        )
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_4(self, client: Steel) -> None:
        environment = client.environments.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            network_secrets=[
                {
                    "domain": "domain",
                    "header": "header",
                    "secret": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "template": "{{secret}}",
                    "port": 1,
                }
            ],
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
            secrets={"foo": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
            spec={
                "auto_pause": True,
                "disk_mib": 1,
                "env": {"foo": "string"},
                "memory_mib": 128,
                "name": "x",
                "network_policy": {
                    "cidrs": {
                        "allow": ["x"],
                        "deny": ["x"],
                    },
                    "domains": {
                        "allow": ["x"],
                        "deny": ["x"],
                    },
                    "internet_access": True,
                },
                "template": "x",
                "timeout_seconds": 1,
                "vcpu": 1,
            },
        )
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    def test_raw_response_update_overload_4(self, client: Steel) -> None:
        response = client.environments.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            network_secrets=[
                {
                    "domain": "domain",
                    "header": "header",
                    "secret": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "template": "{{secret}}",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_4(self, client: Steel) -> None:
        with client.environments.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            network_secrets=[
                {
                    "domain": "domain",
                    "header": "header",
                    "secret": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "template": "{{secret}}",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(Environment, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_4(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.environments.with_raw_response.update(
                id="",
                network_secrets=[
                    {
                        "domain": "domain",
                        "header": "header",
                        "secret": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                        "template": "{{secret}}",
                    }
                ],
            )

    @parametrize
    def test_method_list(self, client: Steel) -> None:
        environment = client.environments.list()
        assert_matches_type(EnvironmentList, environment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Steel) -> None:
        environment = client.environments.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EnvironmentList, environment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Steel) -> None:
        response = client.environments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentList, environment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Steel) -> None:
        with client.environments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentList, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Steel) -> None:
        environment = client.environments.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert environment is None

    @parametrize
    def test_method_delete_with_all_params(self, client: Steel) -> None:
        environment = client.environments.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert environment is None

    @parametrize
    def test_raw_response_delete(self, client: Steel) -> None:
        response = client.environments.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert environment is None

    @parametrize
    def test_streaming_response_delete(self, client: Steel) -> None:
        with client.environments.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert environment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.environments.with_raw_response.delete(
                id="",
            )


class TestAsyncEnvironments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncSteel) -> None:
        environment = await async_client.environments.create(
            name="x",
        )
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSteel) -> None:
        environment = await async_client.environments.create(
            name="x",
            network_secrets=[
                {
                    "domain": "domain",
                    "header": "header",
                    "secret": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "template": "{{secret}}",
                    "port": 1,
                }
            ],
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secrets={"foo": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
            spec={
                "auto_pause": True,
                "disk_mib": 1,
                "env": {"foo": "string"},
                "memory_mib": 128,
                "name": "x",
                "network_policy": {
                    "cidrs": {
                        "allow": ["x"],
                        "deny": ["x"],
                    },
                    "domains": {
                        "allow": ["x"],
                        "deny": ["x"],
                    },
                    "internet_access": True,
                },
                "template": "x",
                "timeout_seconds": 1,
                "vcpu": 1,
            },
        )
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSteel) -> None:
        response = await async_client.environments.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSteel) -> None:
        async with async_client.environments.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(Environment, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSteel) -> None:
        environment = await async_client.environments.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncSteel) -> None:
        environment = await async_client.environments.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSteel) -> None:
        response = await async_client.environments.with_raw_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSteel) -> None:
        async with async_client.environments.with_streaming_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(Environment, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.environments.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncSteel) -> None:
        environment = await async_client.environments.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        )
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncSteel) -> None:
        environment = await async_client.environments.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            network_secrets=[
                {
                    "domain": "domain",
                    "header": "header",
                    "secret": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "template": "{{secret}}",
                    "port": 1,
                }
            ],
            secrets={"foo": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
            spec={
                "auto_pause": True,
                "disk_mib": 1,
                "env": {"foo": "string"},
                "memory_mib": 128,
                "name": "x",
                "network_policy": {
                    "cidrs": {
                        "allow": ["x"],
                        "deny": ["x"],
                    },
                    "domains": {
                        "allow": ["x"],
                        "deny": ["x"],
                    },
                    "internet_access": True,
                },
                "template": "x",
                "timeout_seconds": 1,
                "vcpu": 1,
            },
        )
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncSteel) -> None:
        response = await async_client.environments.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncSteel) -> None:
        async with async_client.environments.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(Environment, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.environments.with_raw_response.update(
                id="",
                name="x",
            )

    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncSteel) -> None:
        environment = await async_client.environments.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            spec={},
        )
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncSteel) -> None:
        environment = await async_client.environments.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            spec={
                "auto_pause": True,
                "disk_mib": 1,
                "env": {"foo": "string"},
                "memory_mib": 128,
                "name": "x",
                "network_policy": {
                    "cidrs": {
                        "allow": ["x"],
                        "deny": ["x"],
                    },
                    "domains": {
                        "allow": ["x"],
                        "deny": ["x"],
                    },
                    "internet_access": True,
                },
                "template": "x",
                "timeout_seconds": 1,
                "vcpu": 1,
            },
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
            network_secrets=[
                {
                    "domain": "domain",
                    "header": "header",
                    "secret": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "template": "{{secret}}",
                    "port": 1,
                }
            ],
            secrets={"foo": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
        )
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncSteel) -> None:
        response = await async_client.environments.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            spec={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncSteel) -> None:
        async with async_client.environments.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            spec={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(Environment, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.environments.with_raw_response.update(
                id="",
                spec={},
            )

    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncSteel) -> None:
        environment = await async_client.environments.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secrets={"foo": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
        )
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_3(self, async_client: AsyncSteel) -> None:
        environment = await async_client.environments.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secrets={"foo": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
            network_secrets=[
                {
                    "domain": "domain",
                    "header": "header",
                    "secret": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "template": "{{secret}}",
                    "port": 1,
                }
            ],
            spec={
                "auto_pause": True,
                "disk_mib": 1,
                "env": {"foo": "string"},
                "memory_mib": 128,
                "name": "x",
                "network_policy": {
                    "cidrs": {
                        "allow": ["x"],
                        "deny": ["x"],
                    },
                    "domains": {
                        "allow": ["x"],
                        "deny": ["x"],
                    },
                    "internet_access": True,
                },
                "template": "x",
                "timeout_seconds": 1,
                "vcpu": 1,
            },
        )
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncSteel) -> None:
        response = await async_client.environments.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secrets={"foo": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_3(self, async_client: AsyncSteel) -> None:
        async with async_client.environments.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secrets={"foo": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(Environment, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_3(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.environments.with_raw_response.update(
                id="",
                secrets={"foo": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
            )

    @parametrize
    async def test_method_update_overload_4(self, async_client: AsyncSteel) -> None:
        environment = await async_client.environments.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            network_secrets=[
                {
                    "domain": "domain",
                    "header": "header",
                    "secret": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "template": "{{secret}}",
                }
            ],
        )
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_4(self, async_client: AsyncSteel) -> None:
        environment = await async_client.environments.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            network_secrets=[
                {
                    "domain": "domain",
                    "header": "header",
                    "secret": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "template": "{{secret}}",
                    "port": 1,
                }
            ],
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
            secrets={"foo": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
            spec={
                "auto_pause": True,
                "disk_mib": 1,
                "env": {"foo": "string"},
                "memory_mib": 128,
                "name": "x",
                "network_policy": {
                    "cidrs": {
                        "allow": ["x"],
                        "deny": ["x"],
                    },
                    "domains": {
                        "allow": ["x"],
                        "deny": ["x"],
                    },
                    "internet_access": True,
                },
                "template": "x",
                "timeout_seconds": 1,
                "vcpu": 1,
            },
        )
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_4(self, async_client: AsyncSteel) -> None:
        response = await async_client.environments.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            network_secrets=[
                {
                    "domain": "domain",
                    "header": "header",
                    "secret": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "template": "{{secret}}",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(Environment, environment, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_4(self, async_client: AsyncSteel) -> None:
        async with async_client.environments.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            network_secrets=[
                {
                    "domain": "domain",
                    "header": "header",
                    "secret": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "template": "{{secret}}",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(Environment, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_4(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.environments.with_raw_response.update(
                id="",
                network_secrets=[
                    {
                        "domain": "domain",
                        "header": "header",
                        "secret": {"secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                        "template": "{{secret}}",
                    }
                ],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSteel) -> None:
        environment = await async_client.environments.list()
        assert_matches_type(EnvironmentList, environment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSteel) -> None:
        environment = await async_client.environments.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EnvironmentList, environment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSteel) -> None:
        response = await async_client.environments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentList, environment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSteel) -> None:
        async with async_client.environments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentList, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncSteel) -> None:
        environment = await async_client.environments.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert environment is None

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncSteel) -> None:
        environment = await async_client.environments.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert environment is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSteel) -> None:
        response = await async_client.environments.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert environment is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSteel) -> None:
        async with async_client.environments.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert environment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.environments.with_raw_response.delete(
                id="",
            )
