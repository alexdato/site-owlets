from mezzanine.conf import register_setting
from django.utils.translation import ugettext_lazy as _

register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    append=True,
    default=("SOCIAL_LINK_FACEBOOK", "SOCIAL_LINK_TWITTER", "PHONE_NUMBER", "COME_AND_VISIT_LINK", "EMAIL", "ADDRESS"),
)

register_setting(
    name="SOCIAL_LINK_FACEBOOK",
    label=_("Facebook link"),
    description=_("If present a Facebook icon linking here will be in the header."),
    editable=True,
    default="https://facebook.com/owlets",
)

register_setting(
	name="SOCIAL_LINK_TWITTER",
	label=_("Twitter link"),
	description=_("If present a Twitter icon linking here will be in the header"),
	editable=True,
	default="https://twitter.com/owlets",
)

register_setting(
	name="PHONE_NUMBER",
	label=_("Nursery phone number"),
	description=_("This is the telephone number which is shown across the site"),
	editable=True,
	default="01323 123456",
)

register_setting (
	name="COME_AND_VISIT_LINK",
	label=_("Come and visit us link"),
	description=_("This is the 'come and visit us' link shown across the site"),
	editable=True,
	default="/visit/",
)

register_setting (
	name="ADDRESS",
	label=_("Address"),
	description=_("The nursery address which is shown in the footer"),
	editable=True,
	default="somewhere",
)

register_setting (
	name="EMAIL",
	label=_("Email address"),
	description=_("The email address which is used in the footer"),
	editable=True,
	default="fiona@owlets.com"
)