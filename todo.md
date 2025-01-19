
## todo

* 기존 ModeMultiTextField(mode-multi-text-field) 에 대해 이름 변경
  * 집/회사/기타를 입력한 다는 것을 강조해서 이름을 정해야 한다.
    * home/work/else ?
* ModeMultiTextField(mode-multi-text-field) 를 복사해서 유사한 구조를 생성한다.
  * 데이터 타입이 enum 일 때 추가하는 기능 필요
  * [{title: "title", value: "value"}] 형태의 리스트 형을 저장해야 한다.
  * 입력이 한 행에 title, value 를 입력할 수 있는 input 이 2개이고 순서 변경이 가능해야 한다. 
  * ModeMultiTextField 가 기본적으로 순서 변경 가능함.



* parse_obj_as  이거 deprecated 됨
  * pydantic.TypeAdapter.json_schema 을 사용해야 한다. 
퍄
* AliasPath and AliasChoices 에 대해 찾아 볼것
  * https://docs.pydantic.dev/latest/concepts/alias/#aliaspath-and-aliaschoices


* MobelPublic, ModelPrivate 는 이것으로도 가능은 한데..
  * https://stackoverflow.com/a/76449131/6652082


## todo 순서
1. category 기능 구현
2. category custom field 기능 필요
3. tag list 기능
4. 사용 시나리오 정리 필요
