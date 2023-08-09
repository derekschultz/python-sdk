# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: proto/resource/v1/resource.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    Dict,
    List,
    Optional,
)

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


class ResourceType(betterproto.Enum):
    Api = 0
    Function = 1
    Bucket = 2
    Queue = 3
    Topic = 4
    Schedule = 5
    Subscription = 6
    Collection = 7
    Policy = 8
    Secret = 9
    Notification = 10
    Websocket = 11
    Http = 12


class Action(betterproto.Enum):
    BucketFileList = 0
    """Bucket Permissions: 0XX"""

    BucketFileGet = 1
    BucketFilePut = 2
    BucketFileDelete = 3
    TopicList = 200
    """Topic Permissions: 2XX"""

    TopicDetail = 201
    TopicEventPublish = 202
    QueueSend = 300
    """Queue Permissions: 3XX"""

    QueueReceive = 301
    QueueList = 302
    QueueDetail = 303
    CollectionDocumentRead = 400
    """Collection Permissions: 4XX"""

    CollectionDocumentWrite = 401
    CollectionDocumentDelete = 402
    CollectionQuery = 403
    CollectionList = 404
    SecretPut = 500
    """Secret Permissions: 5XX"""

    SecretAccess = 501
    WebsocketManage = 600
    """Websocket Permissions: 6XX"""


@dataclass(eq=False, repr=False)
class PolicyResource(betterproto.Message):
    principals: List["Resource"] = betterproto.message_field(1)
    actions: List["Action"] = betterproto.enum_field(2)
    resources: List["Resource"] = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class Resource(betterproto.Message):
    type: "ResourceType" = betterproto.enum_field(1)
    name: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class ResourceDeclareRequest(betterproto.Message):
    resource: "Resource" = betterproto.message_field(1)
    policy: "PolicyResource" = betterproto.message_field(10, group="config")
    bucket: "BucketResource" = betterproto.message_field(11, group="config")
    queue: "QueueResource" = betterproto.message_field(12, group="config")
    topic: "TopicResource" = betterproto.message_field(13, group="config")
    collection: "CollectionResource" = betterproto.message_field(14, group="config")
    secret: "SecretResource" = betterproto.message_field(15, group="config")
    api: "ApiResource" = betterproto.message_field(16, group="config")


@dataclass(eq=False, repr=False)
class BucketResource(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class QueueResource(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class TopicResource(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class CollectionResource(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class SecretResource(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class ApiSecurityDefinitionJwt(betterproto.Message):
    """protect your API with JWT authentication"""

    issuer: str = betterproto.string_field(1)
    audiences: List[str] = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class ApiSecurityDefinition(betterproto.Message):
    jwt: "ApiSecurityDefinitionJwt" = betterproto.message_field(1, group="definition")


@dataclass(eq=False, repr=False)
class ApiScopes(betterproto.Message):
    scopes: List[str] = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class ApiResource(betterproto.Message):
    security_definitions: Dict[str, "ApiSecurityDefinition"] = betterproto.map_field(
        1, betterproto.TYPE_STRING, betterproto.TYPE_MESSAGE
    )
    """
    Security definitions for the api These may be used by registered routes and
    operations on the API
    """

    security: Dict[str, "ApiScopes"] = betterproto.map_field(
        2, betterproto.TYPE_STRING, betterproto.TYPE_MESSAGE
    )
    """root level security for this api"""


@dataclass(eq=False, repr=False)
class ResourceDeclareResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class ApiResourceDetails(betterproto.Message):
    url: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class WebsocketResourceDetails(betterproto.Message):
    url: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class ResourceDetailsRequest(betterproto.Message):
    resource: "Resource" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class ResourceDetailsResponse(betterproto.Message):
    id: str = betterproto.string_field(1)
    """The identifier of the resource"""

    provider: str = betterproto.string_field(2)
    """The provider this resource is deployed with (e.g. aws)"""

    service: str = betterproto.string_field(3)
    """The service this resource is deployed on (e.g. ApiGateway)"""

    api: "ApiResourceDetails" = betterproto.message_field(10, group="details")
    websocket: "WebsocketResourceDetails" = betterproto.message_field(
        11, group="details"
    )


class ResourceServiceStub(betterproto.ServiceStub):
    async def declare(
        self,
        resource_declare_request: "ResourceDeclareRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "ResourceDeclareResponse":
        return await self._unary_unary(
            "/nitric.resource.v1.ResourceService/Declare",
            resource_declare_request,
            ResourceDeclareResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def details(
        self,
        resource_details_request: "ResourceDetailsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "ResourceDetailsResponse":
        return await self._unary_unary(
            "/nitric.resource.v1.ResourceService/Details",
            resource_details_request,
            ResourceDetailsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class ResourceServiceBase(ServiceBase):
    async def declare(
        self, resource_declare_request: "ResourceDeclareRequest"
    ) -> "ResourceDeclareResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def details(
        self, resource_details_request: "ResourceDetailsRequest"
    ) -> "ResourceDetailsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_declare(
        self,
        stream: "grpclib.server.Stream[ResourceDeclareRequest, ResourceDeclareResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.declare(request)
        await stream.send_message(response)

    async def __rpc_details(
        self,
        stream: "grpclib.server.Stream[ResourceDetailsRequest, ResourceDetailsResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.details(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/nitric.resource.v1.ResourceService/Declare": grpclib.const.Handler(
                self.__rpc_declare,
                grpclib.const.Cardinality.UNARY_UNARY,
                ResourceDeclareRequest,
                ResourceDeclareResponse,
            ),
            "/nitric.resource.v1.ResourceService/Details": grpclib.const.Handler(
                self.__rpc_details,
                grpclib.const.Cardinality.UNARY_UNARY,
                ResourceDetailsRequest,
                ResourceDetailsResponse,
            ),
        }
