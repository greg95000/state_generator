{% if attributes|length > 0 %}
    def __init__(
        self,
    {%- for attribute, _type in attributes.items() %}
        {{ attribute }}{%if _type %}: {{ _type }}{% endif %}{% if not loop.last %},{% endif %}
    {%- endfor %}
    ) -> None:
    {%- for attribute in attributes %}
        self.{{ attribute }} = {{ attribute }}
    {%- endfor %}
{% else %}
    def __init__(self) -> None:
    {% for attribute in attributes %}
        self.{{ attribute }} = {{ attribute }}
    {% endfor %}
{% endif %}