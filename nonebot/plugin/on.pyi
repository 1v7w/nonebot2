import re
from types import ModuleType
from datetime import datetime, timedelta
from typing import Set, List, Type, Tuple, Union, Optional

from nonebot.adapters import Event
from nonebot.matcher import Matcher
from nonebot.permission import Permission
from nonebot.dependencies import Dependent
from nonebot.rule import Rule, ArgumentParser
from nonebot.typing import T_State, T_Handler, T_RuleChecker, T_PermissionChecker

from .plugin import Plugin

def store_matcher(matcher: Type[Matcher]) -> None: ...
def get_matcher_plugin(depth: int = ...) -> Optional[Plugin]: ...
def get_matcher_module(depth: int = ...) -> Optional[ModuleType]: ...
def on(
    type: str = "",
    rule: Optional[Union[Rule, T_RuleChecker]] = ...,
    permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
    *,
    handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
    temp: bool = ...,
    expire_time: Optional[Union[datetime, timedelta]] = ...,
    priority: int = ...,
    block: bool = ...,
    state: Optional[T_State] = ...,
) -> Type[Matcher]: ...
def on_metaevent(
    rule: Optional[Union[Rule, T_RuleChecker]] = ...,
    permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
    *,
    handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
    temp: bool = ...,
    expire_time: Optional[Union[datetime, timedelta]] = ...,
    priority: int = ...,
    block: bool = ...,
    state: Optional[T_State] = ...,
) -> Type[Matcher]: ...
def on_message(
    rule: Optional[Union[Rule, T_RuleChecker]] = ...,
    permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
    *,
    handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
    temp: bool = ...,
    expire_time: Optional[Union[datetime, timedelta]] = ...,
    priority: int = ...,
    block: bool = ...,
    state: Optional[T_State] = ...,
) -> Type[Matcher]: ...
def on_notice(
    rule: Optional[Union[Rule, T_RuleChecker]] = ...,
    permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
    *,
    handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
    temp: bool = ...,
    expire_time: Optional[Union[datetime, timedelta]] = ...,
    priority: int = ...,
    block: bool = ...,
    state: Optional[T_State] = ...,
) -> Type[Matcher]: ...
def on_request(
    rule: Optional[Union[Rule, T_RuleChecker]] = ...,
    permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
    *,
    handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
    temp: bool = ...,
    expire_time: Optional[Union[datetime, timedelta]] = ...,
    priority: int = ...,
    block: bool = ...,
    state: Optional[T_State] = ...,
) -> Type[Matcher]: ...
def on_startswith(
    msg: Union[str, Tuple[str, ...]],
    rule: Optional[Union[Rule, T_RuleChecker]] = ...,
    ignorecase: bool = ...,
    *,
    permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
    handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
    temp: bool = ...,
    expire_time: Optional[Union[datetime, timedelta]] = ...,
    priority: int = ...,
    block: bool = ...,
    state: Optional[T_State] = ...,
) -> Type[Matcher]: ...
def on_endswith(
    msg: Union[str, Tuple[str, ...]],
    rule: Optional[Union[Rule, T_RuleChecker]] = ...,
    ignorecase: bool = ...,
    *,
    permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
    handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
    temp: bool = ...,
    expire_time: Optional[Union[datetime, timedelta]] = ...,
    priority: int = ...,
    block: bool = ...,
    state: Optional[T_State] = ...,
) -> Type[Matcher]: ...
def on_fullmatch(
    msg: Union[str, Tuple[str, ...]],
    rule: Optional[Union[Rule, T_RuleChecker]] = ...,
    ignorecase: bool = ...,
    *,
    permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
    handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
    temp: bool = ...,
    expire_time: Optional[Union[datetime, timedelta]] = ...,
    priority: int = ...,
    block: bool = ...,
    state: Optional[T_State] = ...,
) -> Type[Matcher]: ...
def on_keyword(
    keywords: Set[str],
    rule: Optional[Union[Rule, T_RuleChecker]] = ...,
    *,
    permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
    handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
    temp: bool = ...,
    expire_time: Optional[Union[datetime, timedelta]] = ...,
    priority: int = ...,
    block: bool = ...,
    state: Optional[T_State] = ...,
) -> Type[Matcher]: ...
def on_command(
    cmd: Union[str, Tuple[str, ...]],
    rule: Optional[Union[Rule, T_RuleChecker]] = ...,
    aliases: Optional[Set[Union[str, Tuple[str, ...]]]] = ...,
    force_whitespace: Optional[Union[str, bool]] = ...,
    *,
    permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
    handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
    temp: bool = ...,
    expire_time: Optional[Union[datetime, timedelta]] = ...,
    priority: int = ...,
    block: bool = ...,
    state: Optional[T_State] = ...,
) -> Type[Matcher]: ...
def on_shell_command(
    cmd: Union[str, Tuple[str, ...]],
    rule: Optional[Union[Rule, T_RuleChecker]] = ...,
    aliases: Optional[Set[Union[str, Tuple[str, ...]]]] = ...,
    parser: Optional[ArgumentParser] = ...,
    *,
    permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
    handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
    temp: bool = ...,
    expire_time: Optional[Union[datetime, timedelta]] = ...,
    priority: int = ...,
    block: bool = ...,
    state: Optional[T_State] = ...,
) -> Type[Matcher]: ...
def on_regex(
    pattern: str,
    flags: Union[int, re.RegexFlag] = ...,
    rule: Optional[Union[Rule, T_RuleChecker]] = ...,
    *,
    permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
    handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
    temp: bool = ...,
    expire_time: Optional[Union[datetime, timedelta]] = ...,
    priority: int = ...,
    block: bool = ...,
    state: Optional[T_State] = ...,
) -> Type[Matcher]: ...
def on_type(
    types: Union[Type[Event], Tuple[Type[Event], ...]],
    rule: Optional[Union[Rule, T_RuleChecker]] = ...,
    *,
    permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
    handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
    temp: bool = ...,
    expire_time: Optional[Union[datetime, timedelta]] = ...,
    priority: int = ...,
    block: bool = ...,
    state: Optional[T_State] = ...,
) -> Type[Matcher]: ...

class CommandGroup:
    def __init__(
        self,
        cmd: Union[str, Tuple[str, ...]],
        *,
        rule: Optional[Union[Rule, T_RuleChecker]] = ...,
        permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
        handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
        temp: bool = ...,
        expire_time: Optional[Union[datetime, timedelta]] = ...,
        priority: int = ...,
        block: bool = ...,
        state: Optional[T_State] = ...,
    ): ...
    def command(
        self,
        cmd: Union[str, Tuple[str, ...]],
        *,
        rule: Optional[Union[Rule, T_RuleChecker]] = ...,
        aliases: Optional[Set[Union[str, Tuple[str, ...]]]] = ...,
        force_whitespace: Optional[Union[str, bool]] = ...,
        permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
        handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
        temp: bool = ...,
        expire_time: Optional[Union[datetime, timedelta]] = ...,
        priority: int = ...,
        block: bool = ...,
        state: Optional[T_State] = ...,
    ) -> Type[Matcher]: ...
    def shell_command(
        self,
        cmd: Union[str, Tuple[str, ...]],
        *,
        rule: Optional[Union[Rule, T_RuleChecker]] = ...,
        aliases: Optional[Set[Union[str, Tuple[str, ...]]]] = ...,
        parser: Optional[ArgumentParser] = ...,
        permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
        handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
        temp: bool = ...,
        expire_time: Optional[Union[datetime, timedelta]] = ...,
        priority: int = ...,
        block: bool = ...,
        state: Optional[T_State] = ...,
    ) -> Type[Matcher]: ...

class MatcherGroup:
    def __init__(
        self,
        *,
        type: str = ...,
        rule: Optional[Union[Rule, T_RuleChecker]] = ...,
        permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
        handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
        temp: bool = ...,
        expire_time: Optional[Union[datetime, timedelta]] = ...,
        priority: int = ...,
        block: bool = ...,
        state: Optional[T_State] = ...,
    ): ...
    def on(
        self,
        *,
        type: str = ...,
        rule: Optional[Union[Rule, T_RuleChecker]] = ...,
        permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
        handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
        temp: bool = ...,
        expire_time: Optional[Union[datetime, timedelta]] = ...,
        priority: int = ...,
        block: bool = ...,
        state: Optional[T_State] = ...,
    ) -> Type[Matcher]: ...
    def on_metaevent(
        self,
        *,
        rule: Optional[Union[Rule, T_RuleChecker]] = ...,
        permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
        handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
        temp: bool = ...,
        expire_time: Optional[Union[datetime, timedelta]] = ...,
        priority: int = ...,
        block: bool = ...,
        state: Optional[T_State] = ...,
    ) -> Type[Matcher]: ...
    def on_message(
        self,
        *,
        rule: Optional[Union[Rule, T_RuleChecker]] = ...,
        permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
        handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
        temp: bool = ...,
        expire_time: Optional[Union[datetime, timedelta]] = ...,
        priority: int = ...,
        block: bool = ...,
        state: Optional[T_State] = ...,
    ) -> Type[Matcher]: ...
    def on_notice(
        self,
        *,
        rule: Optional[Union[Rule, T_RuleChecker]] = ...,
        permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
        handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
        temp: bool = ...,
        expire_time: Optional[Union[datetime, timedelta]] = ...,
        priority: int = ...,
        block: bool = ...,
        state: Optional[T_State] = ...,
    ) -> Type[Matcher]: ...
    def on_request(
        self,
        *,
        rule: Optional[Union[Rule, T_RuleChecker]] = ...,
        permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
        handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
        temp: bool = ...,
        expire_time: Optional[Union[datetime, timedelta]] = ...,
        priority: int = ...,
        block: bool = ...,
        state: Optional[T_State] = ...,
    ) -> Type[Matcher]: ...
    def on_startswith(
        self,
        msg: Union[str, Tuple[str, ...]],
        *,
        ignorecase: bool = ...,
        rule: Optional[Union[Rule, T_RuleChecker]] = ...,
        permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
        handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
        temp: bool = ...,
        expire_time: Optional[Union[datetime, timedelta]] = ...,
        priority: int = ...,
        block: bool = ...,
        state: Optional[T_State] = ...,
    ) -> Type[Matcher]: ...
    def on_endswith(
        self,
        msg: Union[str, Tuple[str, ...]],
        *,
        ignorecase: bool = ...,
        rule: Optional[Union[Rule, T_RuleChecker]] = ...,
        permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
        handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
        temp: bool = ...,
        expire_time: Optional[Union[datetime, timedelta]] = ...,
        priority: int = ...,
        block: bool = ...,
        state: Optional[T_State] = ...,
    ) -> Type[Matcher]: ...
    def on_fullmatch(
        self,
        msg: Union[str, Tuple[str, ...]],
        *,
        ignorecase: bool = ...,
        rule: Optional[Union[Rule, T_RuleChecker]] = ...,
        permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
        handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
        temp: bool = ...,
        expire_time: Optional[Union[datetime, timedelta]] = ...,
        priority: int = ...,
        block: bool = ...,
        state: Optional[T_State] = ...,
    ) -> Type[Matcher]: ...
    def on_keyword(
        self,
        keywords: Set[str],
        *,
        rule: Optional[Union[Rule, T_RuleChecker]] = ...,
        permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
        handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
        temp: bool = ...,
        expire_time: Optional[Union[datetime, timedelta]] = ...,
        priority: int = ...,
        block: bool = ...,
        state: Optional[T_State] = ...,
    ) -> Type[Matcher]: ...
    def on_command(
        self,
        cmd: Union[str, Tuple[str, ...]],
        aliases: Optional[Set[Union[str, Tuple[str, ...]]]] = ...,
        force_whitespace: Optional[Union[str, bool]] = ...,
        *,
        rule: Optional[Union[Rule, T_RuleChecker]] = ...,
        permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
        handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
        temp: bool = ...,
        expire_time: Optional[Union[datetime, timedelta]] = ...,
        priority: int = ...,
        block: bool = ...,
        state: Optional[T_State] = ...,
    ) -> Type[Matcher]: ...
    def on_shell_command(
        self,
        cmd: Union[str, Tuple[str, ...]],
        aliases: Optional[Set[Union[str, Tuple[str, ...]]]] = ...,
        parser: Optional[ArgumentParser] = ...,
        *,
        rule: Optional[Union[Rule, T_RuleChecker]] = ...,
        permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
        handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
        temp: bool = ...,
        expire_time: Optional[Union[datetime, timedelta]] = ...,
        priority: int = ...,
        block: bool = ...,
        state: Optional[T_State] = ...,
    ) -> Type[Matcher]: ...
    def on_regex(
        self,
        pattern: str,
        flags: Union[int, re.RegexFlag] = ...,
        *,
        rule: Optional[Union[Rule, T_RuleChecker]] = ...,
        permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
        handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
        temp: bool = ...,
        expire_time: Optional[Union[datetime, timedelta]] = ...,
        priority: int = ...,
        block: bool = ...,
        state: Optional[T_State] = ...,
    ) -> Type[Matcher]: ...
    def on_type(
        self,
        types: Union[Type[Event], Tuple[Type[Event]]],
        *,
        rule: Optional[Union[Rule, T_RuleChecker]] = ...,
        permission: Optional[Union[Permission, T_PermissionChecker]] = ...,
        handlers: Optional[List[Union[T_Handler, Dependent]]] = ...,
        temp: bool = ...,
        expire_time: Optional[Union[datetime, timedelta]] = ...,
        priority: int = ...,
        block: bool = ...,
        state: Optional[T_State] = ...,
    ) -> Type[Matcher]: ...
