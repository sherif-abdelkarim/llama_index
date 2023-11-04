# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from llama_index.ingestion.client.core.api_error import ApiError
from llama_index.ingestion.client.core.client_wrapper import (
    AsyncClientWrapper,
    SyncClientWrapper,
)
from llama_index.ingestion.client.core.jsonable_encoder import jsonable_encoder
from llama_index.ingestion.client.core.remove_none_from_dict import (
    remove_none_from_dict,
)
from llama_index.ingestion.client.errors.unprocessable_entity_error import (
    UnprocessableEntityError,
)
from llama_index.ingestion.client.types.configured_transformation_execution import (
    ConfiguredTransformationExecution,
)
from llama_index.ingestion.client.types.configured_transformation_item import (
    ConfiguredTransformationItem,
)
from llama_index.ingestion.client.types.data_sink_create import DataSinkCreate
from llama_index.ingestion.client.types.data_source_create import DataSourceCreate
from llama_index.ingestion.client.types.eval_dataset_execution import (
    EvalDatasetExecution,
)
from llama_index.ingestion.client.types.eval_question_result import EvalQuestionResult
from llama_index.ingestion.client.types.http_validation_error import HttpValidationError
from llama_index.ingestion.client.types.pipeline import Pipeline
from llama_index.ingestion.client.types.text_node import TextNode

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class PipelineClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_pipeline_by_name_api_pipeline_get(
        self,
        *,
        pipeline_name: typing.Optional[str] = None,
        project_name: typing.Optional[str] = None,
    ) -> typing.List[Pipeline]:
        """
        Get a pipeline by name.

        Parameters:
            - pipeline_name: typing.Optional[str].

            - project_name: typing.Optional[str].
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "api/pipeline"
            ),
            params=remove_none_from_dict(
                {"pipeline_name": pipeline_name, "project_name": project_name}
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[Pipeline], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_pipeline_for_project(self, pipeline_id: str) -> Pipeline:
        """
        Get a pipeline by ID for a given project.

        Parameters:
            - pipeline_id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/pipeline/{pipeline_id}"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Pipeline, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_existing_pipeline(
        self,
        pipeline_id: str,
        *,
        configured_transformations: typing.Optional[
            typing.List[ConfiguredTransformationItem]
        ] = OMIT,
        data_source_ids: typing.Optional[typing.List[str]] = OMIT,
        data_sources: typing.Optional[typing.List[DataSourceCreate]] = OMIT,
        data_sink_ids: typing.Optional[typing.List[str]] = OMIT,
        data_sinks: typing.Optional[typing.List[DataSinkCreate]] = OMIT,
        name: typing.Optional[str] = OMIT,
    ) -> Pipeline:
        """
        Update an existing pipeline for a project.

        Parameters:
            - pipeline_id: str.

            - configured_transformations: typing.Optional[typing.List[ConfiguredTransformationItem]].

            - data_source_ids: typing.Optional[typing.List[str]]. List of data source IDs. When provided instead of data_sources, the data sources will be looked up by ID.

            - data_sources: typing.Optional[typing.List[DataSourceCreate]]. List of data sources. When provided instead of data_source_ids, the data sources will be created.

            - data_sink_ids: typing.Optional[typing.List[str]]. List of data sink IDs. When provided instead of data_sinks, the data sinks will be looked up by ID.

            - data_sinks: typing.Optional[typing.List[DataSinkCreate]]. List of data sinks. When provided instead of data_sink_ids, the data sinks will be created.

            - name: typing.Optional[str].
        """
        _request: typing.Dict[str, typing.Any] = {}
        if configured_transformations is not OMIT:
            _request["configured_transformations"] = configured_transformations
        if data_source_ids is not OMIT:
            _request["data_source_ids"] = data_source_ids
        if data_sources is not OMIT:
            _request["data_sources"] = data_sources
        if data_sink_ids is not OMIT:
            _request["data_sink_ids"] = data_sink_ids
        if data_sinks is not OMIT:
            _request["data_sinks"] = data_sinks
        if name is not OMIT:
            _request["name"] = name
        _response = self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/pipeline/{pipeline_id}"
            ),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Pipeline, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_all_configured_transformation_executions(
        self, pipeline_id: str
    ) -> typing.List[ConfiguredTransformationExecution]:
        """
        Get all ConfiguredTransformationExecutions for a given pipeline.

        Parameters:
            - pipeline_id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/pipeline/{pipeline_id}/configured_transformation_execution",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[ConfiguredTransformationExecution], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_configured_transformation_execution(
        self,
        pipeline_id: str,
        *,
        configured_transformation_execution_id: typing.Optional[str] = None,
    ) -> ConfiguredTransformationExecution:
        """
        Kick off a new ConfiguredTransformation execution.
        Can optionally supply a configured_transformation_execution_id to run a specific execution.
        In absence of a configured_transformation_execution_id, the last
        configured_transformation_execution will be run (which may end up triggering runs
        for it's prior steps as well).

        Parameters:
            - pipeline_id: str.

            - configured_transformation_execution_id: typing.Optional[str].
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/pipeline/{pipeline_id}/configured_transformation_execution",
            ),
            params=remove_none_from_dict(
                {
                    "configured_transformation_execution_id": configured_transformation_execution_id
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ConfiguredTransformationExecution, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_configured_transformation_execution(
        self, pipeline_id: str, configured_transformation_execution_id: str
    ) -> ConfiguredTransformationExecution:
        """
        Get status of a single pipeline ConfiguredTransformationExecution for a given pipeline.

        Parameters:
            - pipeline_id: str.

            - configured_transformation_execution_id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/pipeline/{pipeline_id}/configured_transformation_execution/{configured_transformation_execution_id}",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ConfiguredTransformationExecution, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_configured_transformation_result(
        self, pipeline_id: str, configured_transformation_id: str
    ) -> typing.List[TextNode]:
        """
        Get the result of an ConfiguredTransformationExecution step.
        Unlike get_configured_transformation_execution_result, this endpoint does
        not check the status of the execution that produced the result for the
        configured_transformation.

        Parameters:
            - pipeline_id: str.

            - configured_transformation_id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/pipeline/{pipeline_id}/configured_transformation/{configured_transformation_id}/result",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[TextNode], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_eval_dataset_executions_api_pipeline_pipeline_id_eval_dataset_execution_get(
        self, pipeline_id: str
    ) -> typing.List[EvalDatasetExecution]:
        """
        Get the status of an EvalDatasetExecution.

        Parameters:
            - pipeline_id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/pipeline/{pipeline_id}/eval_dataset_execution",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[EvalDatasetExecution], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def execute_eval_dataset_api_pipeline_pipeline_id_eval_dataset_execution_post(
        self, pipeline_id: str, *, eval_dataset_id: str, question_ids: typing.List[str]
    ) -> EvalDatasetExecution:
        """
        Execute a dataset.

        Parameters:
            - pipeline_id: str.

            - eval_dataset_id: str.

            - question_ids: typing.List[str].
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/pipeline/{pipeline_id}/eval_dataset_execution",
            ),
            json=jsonable_encoder(
                {"eval_dataset_id": eval_dataset_id, "question_ids": question_ids}
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EvalDatasetExecution, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_eval_dataset_execution(
        self, pipeline_id: str, eval_dataset_execution_id: str
    ) -> EvalDatasetExecution:
        """
        Get the status of an EvalDatasetExecution.

        Parameters:
            - pipeline_id: str.

            - eval_dataset_execution_id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/pipeline/{pipeline_id}/eval_dataset_execution/{eval_dataset_execution_id}",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EvalDatasetExecution, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_eval_question_result(
        self, pipeline_id: str, eval_dataset_id: str, eval_question_id: str
    ) -> EvalQuestionResult:
        """
        Get the result of an EvalQuestionExecution.

        Parameters:
            - pipeline_id: str.

            - eval_dataset_id: str.

            - eval_question_id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/pipeline/{pipeline_id}/eval_dataset/{eval_dataset_id}/eval_question/{eval_question_id}/result",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EvalQuestionResult, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncPipelineClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_pipeline_by_name_api_pipeline_get(
        self,
        *,
        pipeline_name: typing.Optional[str] = None,
        project_name: typing.Optional[str] = None,
    ) -> typing.List[Pipeline]:
        """
        Get a pipeline by name.

        Parameters:
            - pipeline_name: typing.Optional[str].

            - project_name: typing.Optional[str].
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "api/pipeline"
            ),
            params=remove_none_from_dict(
                {"pipeline_name": pipeline_name, "project_name": project_name}
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[Pipeline], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_pipeline_for_project(self, pipeline_id: str) -> Pipeline:
        """
        Get a pipeline by ID for a given project.

        Parameters:
            - pipeline_id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/pipeline/{pipeline_id}"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Pipeline, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_existing_pipeline(
        self,
        pipeline_id: str,
        *,
        configured_transformations: typing.Optional[
            typing.List[ConfiguredTransformationItem]
        ] = OMIT,
        data_source_ids: typing.Optional[typing.List[str]] = OMIT,
        data_sources: typing.Optional[typing.List[DataSourceCreate]] = OMIT,
        data_sink_ids: typing.Optional[typing.List[str]] = OMIT,
        data_sinks: typing.Optional[typing.List[DataSinkCreate]] = OMIT,
        name: typing.Optional[str] = OMIT,
    ) -> Pipeline:
        """
        Update an existing pipeline for a project.

        Parameters:
            - pipeline_id: str.

            - configured_transformations: typing.Optional[typing.List[ConfiguredTransformationItem]].

            - data_source_ids: typing.Optional[typing.List[str]]. List of data source IDs. When provided instead of data_sources, the data sources will be looked up by ID.

            - data_sources: typing.Optional[typing.List[DataSourceCreate]]. List of data sources. When provided instead of data_source_ids, the data sources will be created.

            - data_sink_ids: typing.Optional[typing.List[str]]. List of data sink IDs. When provided instead of data_sinks, the data sinks will be looked up by ID.

            - data_sinks: typing.Optional[typing.List[DataSinkCreate]]. List of data sinks. When provided instead of data_sink_ids, the data sinks will be created.

            - name: typing.Optional[str].
        """
        _request: typing.Dict[str, typing.Any] = {}
        if configured_transformations is not OMIT:
            _request["configured_transformations"] = configured_transformations
        if data_source_ids is not OMIT:
            _request["data_source_ids"] = data_source_ids
        if data_sources is not OMIT:
            _request["data_sources"] = data_sources
        if data_sink_ids is not OMIT:
            _request["data_sink_ids"] = data_sink_ids
        if data_sinks is not OMIT:
            _request["data_sinks"] = data_sinks
        if name is not OMIT:
            _request["name"] = name
        _response = await self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/pipeline/{pipeline_id}"
            ),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Pipeline, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_all_configured_transformation_executions(
        self, pipeline_id: str
    ) -> typing.List[ConfiguredTransformationExecution]:
        """
        Get all ConfiguredTransformationExecutions for a given pipeline.

        Parameters:
            - pipeline_id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/pipeline/{pipeline_id}/configured_transformation_execution",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[ConfiguredTransformationExecution], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_configured_transformation_execution(
        self,
        pipeline_id: str,
        *,
        configured_transformation_execution_id: typing.Optional[str] = None,
    ) -> ConfiguredTransformationExecution:
        """
        Kick off a new ConfiguredTransformation execution.
        Can optionally supply a configured_transformation_execution_id to run a specific execution.
        In absence of a configured_transformation_execution_id, the last
        configured_transformation_execution will be run (which may end up triggering runs
        for it's prior steps as well).

        Parameters:
            - pipeline_id: str.

            - configured_transformation_execution_id: typing.Optional[str].
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/pipeline/{pipeline_id}/configured_transformation_execution",
            ),
            params=remove_none_from_dict(
                {
                    "configured_transformation_execution_id": configured_transformation_execution_id
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ConfiguredTransformationExecution, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_configured_transformation_execution(
        self, pipeline_id: str, configured_transformation_execution_id: str
    ) -> ConfiguredTransformationExecution:
        """
        Get status of a single pipeline ConfiguredTransformationExecution for a given pipeline.

        Parameters:
            - pipeline_id: str.

            - configured_transformation_execution_id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/pipeline/{pipeline_id}/configured_transformation_execution/{configured_transformation_execution_id}",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ConfiguredTransformationExecution, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_configured_transformation_result(
        self, pipeline_id: str, configured_transformation_id: str
    ) -> typing.List[TextNode]:
        """
        Get the result of an ConfiguredTransformationExecution step.
        Unlike get_configured_transformation_execution_result, this endpoint does
        not check the status of the execution that produced the result for the
        configured_transformation.

        Parameters:
            - pipeline_id: str.

            - configured_transformation_id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/pipeline/{pipeline_id}/configured_transformation/{configured_transformation_id}/result",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[TextNode], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_eval_dataset_executions_api_pipeline_pipeline_id_eval_dataset_execution_get(
        self, pipeline_id: str
    ) -> typing.List[EvalDatasetExecution]:
        """
        Get the status of an EvalDatasetExecution.

        Parameters:
            - pipeline_id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/pipeline/{pipeline_id}/eval_dataset_execution",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[EvalDatasetExecution], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def execute_eval_dataset_api_pipeline_pipeline_id_eval_dataset_execution_post(
        self, pipeline_id: str, *, eval_dataset_id: str, question_ids: typing.List[str]
    ) -> EvalDatasetExecution:
        """
        Execute a dataset.

        Parameters:
            - pipeline_id: str.

            - eval_dataset_id: str.

            - question_ids: typing.List[str].
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/pipeline/{pipeline_id}/eval_dataset_execution",
            ),
            json=jsonable_encoder(
                {"eval_dataset_id": eval_dataset_id, "question_ids": question_ids}
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EvalDatasetExecution, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_eval_dataset_execution(
        self, pipeline_id: str, eval_dataset_execution_id: str
    ) -> EvalDatasetExecution:
        """
        Get the status of an EvalDatasetExecution.

        Parameters:
            - pipeline_id: str.

            - eval_dataset_execution_id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/pipeline/{pipeline_id}/eval_dataset_execution/{eval_dataset_execution_id}",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EvalDatasetExecution, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_eval_question_result(
        self, pipeline_id: str, eval_dataset_id: str, eval_question_id: str
    ) -> EvalQuestionResult:
        """
        Get the result of an EvalQuestionExecution.

        Parameters:
            - pipeline_id: str.

            - eval_dataset_id: str.

            - eval_question_id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/pipeline/{pipeline_id}/eval_dataset/{eval_dataset_id}/eval_question/{eval_question_id}/result",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EvalQuestionResult, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
