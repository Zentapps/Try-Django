def generate_form_errors(args, formset=False):
    message = ""
    if not formset:
        for field in args:
            if field.errors:
                message += field.label + " : "
                error = field.errors[0]
                message += str(error)
                message += "\n"

        for err in args.non_field_errors():
            error = err
            message += str(error)
            message += "\n"
    elif formset:
        for form in args:
            for field in form:
                if field.errors:
                    message += field.label + " : "
                    error = field.errors[0]
                    message += str(error)
                    message += "\n"
            for err in form.non_field_errors():
                error = err
                message += str(error)
                message += "\n"

    return message
