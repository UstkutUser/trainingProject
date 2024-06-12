from src.masks import mask_account, mask_card


def mask_card_and_account(acc_number: str) -> str:
    """Возвращет исходную строку с замаскированным номером карты/счета"""
    if acc_number.lower().startswith("счет"):
        account = "".join([i for i in acc_number if i.isdigit()])
        return f"Счет {mask_account(account)}"
    else:
        card_name = " ".join([i for i in acc_number.split() if i.isalpha()])
        card_number = mask_card(
            "".join([i for i in acc_number.split() if i.isdigit()])
        )
        return f"{card_name + " " + card_number}"


def get_data (date_and_time: str) -> str:
    """Возвращает строку с датой в виде дд.мм.гггг"""
    date = [i for i in date_and_time.split("T")]
    return ".".join(list(reversed([i for i in date[0].split("-")])))


if __name__ == "__main__":
    print(mask_card_and_account("Счет 73654108430135874305"))
    print(mask_card_and_account("Visa Platinum 7000 7922 8960 6361"))
