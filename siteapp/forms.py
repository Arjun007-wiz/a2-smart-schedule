from django import forms


class InterestForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "you@example.com",
                "autocomplete": "email",
            }
        ),
    )
    games = forms.CharField(
        label="Games you want to play",
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "e.g. Catan, Valorant, pickup basketball"},
        ),
    )
    availability_note = forms.CharField(
        label="When you're usually free",
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": 3,
                "placeholder": "e.g. weekday evenings PST, weekends",
            }
        ),
    )
