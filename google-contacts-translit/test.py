import argparse
import logging
import atom.data
import gdata.data
import gdata.contacts.client
import gdata.contacts.data
from translit import transliterate

from oauth2client import tools, client
from oauth2client.file import Storage

parser = argparse.ArgumentParser(parents=[tools.argparser])
parser.add_argument('args', nargs=argparse.REMAINDER)
flags = parser.parse_args()
flags.noauth_local_webserver = True

store = Storage("/tmp/cred")

credentials = store.get()

if not credentials or credentials.invalid:
    flow = client.flow_from_clientsecrets(
        "/home/prius/Downloads/client_id.json",
        ["https://www.google.com/m8/feeds/"],
    )

    credentials = tools.run_flow(flow, store, flags)

auth2token = gdata.gauth.OAuth2TokenFromCredentials(credentials)
gd_client = gdata.contacts.client.ContactsClient(source='contacts-to-latin')
gd_client = auth2token.authorize(gd_client)

feed = gd_client.GetContacts(max_results=999999)

for contact in feed.entry:
    contact_changed = False
    if contact.name is not None:
        if "additional_name" in contact.name.__dict__ and \
            contact.name.additional_name is not None:
            if contact.name.additional_name.text != \
                transliterate(contact.name.additional_name.text):
                contact.name.additional_name.text = \
                    transliterate(contact.name.additional_name.text)
                contact_changed = True
        if "family_name" in contact.name.__dict__ and \
            contact.name.family_name is not None:
            if contact.name.family_name.text != \
                transliterate(contact.name.family_name.text):
                contact.name.family_name.text = \
                    transliterate(contact.name.family_name.text)
                contact_changed = True
        if "given_name" in contact.name.__dict__ and \
            contact.name.given_name is not None:
            if contact.name.given_name.text != \
                transliterate(contact.name.given_name.text):
                contact.name.given_name.text = \
                    transliterate(contact.name.given_name.text)
                contact_changed = True
        if "full_name" in contact.name.__dict__ and \
            contact.name.full_name is not None:
            if contact.name.full_name.text != \
                transliterate(contact.name.full_name.text):
                contact.name.full_name.text = \
                    transliterate(contact.name.full_name.text)
                contact_changed = True

    if contact_changed:
        print(contact)
        gd_client.Update(contact)
