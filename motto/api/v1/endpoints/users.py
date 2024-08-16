from fastapi import APIRouter, HTTPException, Request
from motto.models.user import User

router = APIRouter()

user_list = []

@router.get("/")
def test(request: Request):
    print(request.headers.get("user-agent"))
    return request.headers.get("user-agent") 

@router.get("/users")
async def access_users(a: int = 0, b: str = "test b"):
    return {"a": a, "b": b}


@router.get("/users/{name}")
async def user_info(name):
    return name


def decompose_hangul(word):
    if not (ord('가') <= ord(word) <= ord('힣')):
        raise HTTPException(
            status_code=400,
            detail=f"'{word}'는 한글 음절이 아닙니다."
        )
    CHOSEONG = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
    JUNGSEONG = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"
    JONGSEONG = " ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"

    LEN_JUNGSEONG = len(JUNGSEONG)
    LEN_JONGSEONG = len(JONGSEONG)

    for c in word:
        c_num = ord(c) - ord("가")

        cho = (c_num // LEN_JONGSEONG) // LEN_JUNGSEONG
        jung = (c_num // LEN_JONGSEONG) % LEN_JUNGSEONG
        jong = c_num % LEN_JONGSEONG
        if jong == 0:
            return [CHOSEONG[cho], JUNGSEONG[jung]]
        return [CHOSEONG[cho], JUNGSEONG[jung], JONGSEONG[jong]]

        # print(f"{CHOSEONG[cho]}({cho}), {JUNGSEONG[jung]}({jung}), {JONGSEONG[jong]}({jong}), ")


def decompose_name(name):
    decomposed = [decompose_hangul(w) for w in name]
    return decomposed


@router.post("/users")
async def save_user(user: User) -> dict:
    return {"result": decompose_name(user.name)}
