# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from steel import Steel, AsyncSteel
from steel.types import (
    Computer,
    Checkpoint,
    ExecResult,
    ComputerList,
    ComputerQuota,
    ComputerTransitions,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestComputers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Steel) -> None:
        computer = client.computers.create()
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Steel) -> None:
        computer = client.computers.create(
            auto_pause=True,
            disk_mib=1,
            env={"foo": "string"},
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idle_timeout_seconds=0,
            memory_mib=128,
            name="x",
            network_policy={
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
            network_secrets=[
                {
                    "domain": "domain",
                    "header": "header",
                    "secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "template": "{{secret}}",
                    "port": 1,
                }
            ],
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secrets={"foo": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            template="x",
            timeout_seconds=1,
            vcpu=1,
        )
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Steel) -> None:
        response = client.computers.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Steel) -> None:
        with client.computers.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(Computer, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Steel) -> None:
        computer = client.computers.retrieve(
            "x",
        )
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Steel) -> None:
        response = client.computers.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Steel) -> None:
        with client.computers.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(Computer, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Steel) -> None:
        computer = client.computers.list()
        assert_matches_type(ComputerList, computer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Steel) -> None:
        response = client.computers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ComputerList, computer, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Steel) -> None:
        with client.computers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ComputerList, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Steel) -> None:
        computer = client.computers.delete(
            "x",
        )
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Steel) -> None:
        response = client.computers.with_raw_response.delete(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Steel) -> None:
        with client.computers.with_streaming_response.delete(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(Computer, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_create_checkpoint(self, client: Steel) -> None:
        computer = client.computers.create_checkpoint(
            id="x",
        )
        assert_matches_type(Checkpoint, computer, path=["response"])

    @parametrize
    def test_method_create_checkpoint_with_all_params(self, client: Steel) -> None:
        computer = client.computers.create_checkpoint(
            id="x",
            name="x",
        )
        assert_matches_type(Checkpoint, computer, path=["response"])

    @parametrize
    def test_raw_response_create_checkpoint(self, client: Steel) -> None:
        response = client.computers.with_raw_response.create_checkpoint(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(Checkpoint, computer, path=["response"])

    @parametrize
    def test_streaming_response_create_checkpoint(self, client: Steel) -> None:
        with client.computers.with_streaming_response.create_checkpoint(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(Checkpoint, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_checkpoint(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.create_checkpoint(
                id="",
            )

    @parametrize
    def test_method_exec(self, client: Steel) -> None:
        computer = client.computers.exec(
            id="cmp_xntfcnxhnn2xndym4jmmxnzsan2h1",
        )
        assert_matches_type(ExecResult, computer, path=["response"])

    @parametrize
    def test_method_exec_with_all_params(self, client: Steel) -> None:
        computer = client.computers.exec(
            id="cmp_xntfcnxhnn2xndym4jmmxnzsan2h1",
            argv=["string"],
            command="x",
            cwd="x",
            env={"foo": "string"},
            timeout_seconds=1,
        )
        assert_matches_type(ExecResult, computer, path=["response"])

    @parametrize
    def test_raw_response_exec(self, client: Steel) -> None:
        response = client.computers.with_raw_response.exec(
            id="cmp_xntfcnxhnn2xndym4jmmxnzsan2h1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ExecResult, computer, path=["response"])

    @parametrize
    def test_streaming_response_exec(self, client: Steel) -> None:
        with client.computers.with_streaming_response.exec(
            id="cmp_xntfcnxhnn2xndym4jmmxnzsan2h1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ExecResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_exec(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.exec(
                id="",
            )

    @parametrize
    def test_method_pause(self, client: Steel) -> None:
        computer = client.computers.pause(
            "x",
        )
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    def test_raw_response_pause(self, client: Steel) -> None:
        response = client.computers.with_raw_response.pause(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    def test_streaming_response_pause(self, client: Steel) -> None:
        with client.computers.with_streaming_response.pause(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(Computer, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_pause(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.pause(
                "",
            )

    @parametrize
    def test_method_quota(self, client: Steel) -> None:
        computer = client.computers.quota()
        assert_matches_type(ComputerQuota, computer, path=["response"])

    @parametrize
    def test_raw_response_quota(self, client: Steel) -> None:
        response = client.computers.with_raw_response.quota()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ComputerQuota, computer, path=["response"])

    @parametrize
    def test_streaming_response_quota(self, client: Steel) -> None:
        with client.computers.with_streaming_response.quota() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ComputerQuota, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_restart(self, client: Steel) -> None:
        computer = client.computers.restart(
            "x",
        )
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    def test_raw_response_restart(self, client: Steel) -> None:
        response = client.computers.with_raw_response.restart(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    def test_streaming_response_restart(self, client: Steel) -> None:
        with client.computers.with_streaming_response.restart(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(Computer, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_restart(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.restart(
                "",
            )

    @parametrize
    def test_method_resume(self, client: Steel) -> None:
        computer = client.computers.resume(
            "x",
        )
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    def test_raw_response_resume(self, client: Steel) -> None:
        response = client.computers.with_raw_response.resume(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    def test_streaming_response_resume(self, client: Steel) -> None:
        with client.computers.with_streaming_response.resume(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(Computer, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_resume(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.resume(
                "",
            )

    @parametrize
    def test_method_start(self, client: Steel) -> None:
        computer = client.computers.start(
            "x",
        )
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    def test_raw_response_start(self, client: Steel) -> None:
        response = client.computers.with_raw_response.start(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    def test_streaming_response_start(self, client: Steel) -> None:
        with client.computers.with_streaming_response.start(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(Computer, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_start(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.start(
                "",
            )

    @parametrize
    def test_method_stop(self, client: Steel) -> None:
        computer = client.computers.stop(
            "x",
        )
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    def test_raw_response_stop(self, client: Steel) -> None:
        response = client.computers.with_raw_response.stop(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    def test_streaming_response_stop(self, client: Steel) -> None:
        with client.computers.with_streaming_response.stop(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(Computer, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_stop(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.stop(
                "",
            )

    @parametrize
    def test_method_transitions(self, client: Steel) -> None:
        computer = client.computers.transitions(
            "x",
        )
        assert_matches_type(ComputerTransitions, computer, path=["response"])

    @parametrize
    def test_raw_response_transitions(self, client: Steel) -> None:
        response = client.computers.with_raw_response.transitions(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ComputerTransitions, computer, path=["response"])

    @parametrize
    def test_streaming_response_transitions(self, client: Steel) -> None:
        with client.computers.with_streaming_response.transitions(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ComputerTransitions, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_transitions(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.computers.with_raw_response.transitions(
                "",
            )


class TestAsyncComputers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncSteel) -> None:
        computer = await async_client.computers.create()
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSteel) -> None:
        computer = await async_client.computers.create(
            auto_pause=True,
            disk_mib=1,
            env={"foo": "string"},
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idle_timeout_seconds=0,
            memory_mib=128,
            name="x",
            network_policy={
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
            network_secrets=[
                {
                    "domain": "domain",
                    "header": "header",
                    "secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "template": "{{secret}}",
                    "port": 1,
                }
            ],
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secrets={"foo": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            template="x",
            timeout_seconds=1,
            vcpu=1,
        )
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSteel) -> None:
        response = await async_client.computers.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSteel) -> None:
        async with async_client.computers.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(Computer, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSteel) -> None:
        computer = await async_client.computers.retrieve(
            "x",
        )
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSteel) -> None:
        response = await async_client.computers.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSteel) -> None:
        async with async_client.computers.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(Computer, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSteel) -> None:
        computer = await async_client.computers.list()
        assert_matches_type(ComputerList, computer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSteel) -> None:
        response = await async_client.computers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ComputerList, computer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSteel) -> None:
        async with async_client.computers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ComputerList, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncSteel) -> None:
        computer = await async_client.computers.delete(
            "x",
        )
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSteel) -> None:
        response = await async_client.computers.with_raw_response.delete(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSteel) -> None:
        async with async_client.computers.with_streaming_response.delete(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(Computer, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_create_checkpoint(self, async_client: AsyncSteel) -> None:
        computer = await async_client.computers.create_checkpoint(
            id="x",
        )
        assert_matches_type(Checkpoint, computer, path=["response"])

    @parametrize
    async def test_method_create_checkpoint_with_all_params(self, async_client: AsyncSteel) -> None:
        computer = await async_client.computers.create_checkpoint(
            id="x",
            name="x",
        )
        assert_matches_type(Checkpoint, computer, path=["response"])

    @parametrize
    async def test_raw_response_create_checkpoint(self, async_client: AsyncSteel) -> None:
        response = await async_client.computers.with_raw_response.create_checkpoint(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(Checkpoint, computer, path=["response"])

    @parametrize
    async def test_streaming_response_create_checkpoint(self, async_client: AsyncSteel) -> None:
        async with async_client.computers.with_streaming_response.create_checkpoint(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(Checkpoint, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_checkpoint(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.create_checkpoint(
                id="",
            )

    @parametrize
    async def test_method_exec(self, async_client: AsyncSteel) -> None:
        computer = await async_client.computers.exec(
            id="cmp_xntfcnxhnn2xndym4jmmxnzsan2h1",
        )
        assert_matches_type(ExecResult, computer, path=["response"])

    @parametrize
    async def test_method_exec_with_all_params(self, async_client: AsyncSteel) -> None:
        computer = await async_client.computers.exec(
            id="cmp_xntfcnxhnn2xndym4jmmxnzsan2h1",
            argv=["string"],
            command="x",
            cwd="x",
            env={"foo": "string"},
            timeout_seconds=1,
        )
        assert_matches_type(ExecResult, computer, path=["response"])

    @parametrize
    async def test_raw_response_exec(self, async_client: AsyncSteel) -> None:
        response = await async_client.computers.with_raw_response.exec(
            id="cmp_xntfcnxhnn2xndym4jmmxnzsan2h1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ExecResult, computer, path=["response"])

    @parametrize
    async def test_streaming_response_exec(self, async_client: AsyncSteel) -> None:
        async with async_client.computers.with_streaming_response.exec(
            id="cmp_xntfcnxhnn2xndym4jmmxnzsan2h1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ExecResult, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_exec(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.exec(
                id="",
            )

    @parametrize
    async def test_method_pause(self, async_client: AsyncSteel) -> None:
        computer = await async_client.computers.pause(
            "x",
        )
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    async def test_raw_response_pause(self, async_client: AsyncSteel) -> None:
        response = await async_client.computers.with_raw_response.pause(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    async def test_streaming_response_pause(self, async_client: AsyncSteel) -> None:
        async with async_client.computers.with_streaming_response.pause(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(Computer, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_pause(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.pause(
                "",
            )

    @parametrize
    async def test_method_quota(self, async_client: AsyncSteel) -> None:
        computer = await async_client.computers.quota()
        assert_matches_type(ComputerQuota, computer, path=["response"])

    @parametrize
    async def test_raw_response_quota(self, async_client: AsyncSteel) -> None:
        response = await async_client.computers.with_raw_response.quota()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ComputerQuota, computer, path=["response"])

    @parametrize
    async def test_streaming_response_quota(self, async_client: AsyncSteel) -> None:
        async with async_client.computers.with_streaming_response.quota() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ComputerQuota, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_restart(self, async_client: AsyncSteel) -> None:
        computer = await async_client.computers.restart(
            "x",
        )
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    async def test_raw_response_restart(self, async_client: AsyncSteel) -> None:
        response = await async_client.computers.with_raw_response.restart(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    async def test_streaming_response_restart(self, async_client: AsyncSteel) -> None:
        async with async_client.computers.with_streaming_response.restart(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(Computer, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_restart(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.restart(
                "",
            )

    @parametrize
    async def test_method_resume(self, async_client: AsyncSteel) -> None:
        computer = await async_client.computers.resume(
            "x",
        )
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    async def test_raw_response_resume(self, async_client: AsyncSteel) -> None:
        response = await async_client.computers.with_raw_response.resume(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    async def test_streaming_response_resume(self, async_client: AsyncSteel) -> None:
        async with async_client.computers.with_streaming_response.resume(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(Computer, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_resume(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.resume(
                "",
            )

    @parametrize
    async def test_method_start(self, async_client: AsyncSteel) -> None:
        computer = await async_client.computers.start(
            "x",
        )
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    async def test_raw_response_start(self, async_client: AsyncSteel) -> None:
        response = await async_client.computers.with_raw_response.start(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncSteel) -> None:
        async with async_client.computers.with_streaming_response.start(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(Computer, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_start(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.start(
                "",
            )

    @parametrize
    async def test_method_stop(self, async_client: AsyncSteel) -> None:
        computer = await async_client.computers.stop(
            "x",
        )
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncSteel) -> None:
        response = await async_client.computers.with_raw_response.stop(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(Computer, computer, path=["response"])

    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncSteel) -> None:
        async with async_client.computers.with_streaming_response.stop(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(Computer, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_stop(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.stop(
                "",
            )

    @parametrize
    async def test_method_transitions(self, async_client: AsyncSteel) -> None:
        computer = await async_client.computers.transitions(
            "x",
        )
        assert_matches_type(ComputerTransitions, computer, path=["response"])

    @parametrize
    async def test_raw_response_transitions(self, async_client: AsyncSteel) -> None:
        response = await async_client.computers.with_raw_response.transitions(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ComputerTransitions, computer, path=["response"])

    @parametrize
    async def test_streaming_response_transitions(self, async_client: AsyncSteel) -> None:
        async with async_client.computers.with_streaming_response.transitions(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ComputerTransitions, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_transitions(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.computers.with_raw_response.transitions(
                "",
            )
