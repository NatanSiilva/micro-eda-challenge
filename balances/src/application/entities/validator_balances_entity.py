from src.application.shared.validator import ValidatorRoles


class ValidatorBalances:
    def validator(self, entity):
        ValidatorRoles.values(entity._account_id, "account_id").required().string().max_length(255)
        ValidatorRoles.values(entity._balance, "balance").required().integer()