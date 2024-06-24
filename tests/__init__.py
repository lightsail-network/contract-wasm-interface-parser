from unittest import TestCase

from contract_wasm_interface_parser import parse_contract_metadata, ContractMetaData
from stellar_sdk.xdr import *


class TestParse(TestCase):

    def test_parser(self):
        wasm = "AGFzbQEAAAABFQRgAn5+AX5gA35+fgF+YAABfmAAAAIZBAFsATAAAAFsATEAAAFsAV8AAQFsATgAAAMFBAIDAwMFAwEAEAYZA38BQYCAwAALfwBBgIDAAAt/AEGAgMAACwc1BQZtZW1vcnkCAAlpbmNyZW1lbnQABAFfAAcKX19kYXRhX2VuZAMBC19faGVhcF9iYXNlAwIKpwEEkgECAX8BfkEAIQACQAJAAkBCjrrQr4bUOUICEICAgIAAQgFSDQBCjrrQr4bUOUICEIGAgIAAIgFC/wGDQgRSDQEgAUIgiKchAAsgAEEBaiIARQ0BQo660K+G1DkgAK1CIIZCBIQiAUICEIKAgIAAGkKEgICAoAZChICAgMAMEIOAgIAAGiABDwsAAAsQhYCAgAAACwkAEIaAgIAAAAsEAAAACwIACwBzDmNvbnRyYWN0c3BlY3YwAAAAAAAAAEBJbmNyZW1lbnQgaW5jcmVtZW50cyBhbiBpbnRlcm5hbCBjb3VudGVyLCBhbmQgcmV0dXJucyB0aGUgdmFsdWUuAAAACWluY3JlbWVudAAAAAAAAAAAAAABAAAABAAeEWNvbnRyYWN0ZW52bWV0YXYwAAAAAAAAABQAAAAAAG8OY29udHJhY3RtZXRhdjAAAAAAAAAABXJzdmVyAAAAAAAABjEuNzguMAAAAAAAAAAAAAhyc3Nka3ZlcgAAAC8yMC4zLjEjYmEwNDVhNTdhZjk3MWZjODNlNDc1NzQ2YjU5YTUwM2I3ZWY0MTY0OQA="
        metadata = parse_contract_metadata(wasm)
        expected = ContractMetaData(
            env_meta_base64=b"\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00",
            env_meta=[
                SCEnvMetaEntry(
                    kind=SCEnvMetaKind.SC_ENV_META_KIND_INTERFACE_VERSION,
                    interface_version=Uint64(uint64=85899345920),
                )
            ],
            meta_base64=b"\x00\x00\x00\x00\x00\x00\x00\x05rsver\x00\x00\x00\x00\x00\x00\x061.78.0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08rssdkver\x00\x00\x00/20.3.1#ba045a57af971fc83e475746b59a503b7ef41649\x00",
            meta=[
                SCMetaEntry(
                    kind=SCMetaKind.SC_META_V0, v0=SCMetaV0(key=b"rsver", val=b"1.78.0")
                ),
                SCMetaEntry(
                    kind=SCMetaKind.SC_META_V0,
                    v0=SCMetaV0(
                        key=b"rssdkver",
                        val=b"20.3.1#ba045a57af971fc83e475746b59a503b7ef41649",
                    ),
                ),
            ],
            spec_base64=b"\x00\x00\x00\x00\x00\x00\x00@Increment increments an internal counter, and returns the value.\x00\x00\x00\tincrement\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x04",
            spec=[
                SCSpecEntry(
                    kind=SCSpecEntryKind.SC_SPEC_ENTRY_FUNCTION_V0,
                    function_v0=SCSpecFunctionV0(
                        doc=b"Increment increments an internal counter, and returns the value.",
                        name=SCSymbol(sc_symbol=b"increment"),
                        inputs=[],
                        outputs=[SCSpecTypeDef(type=SCSpecType.SC_SPEC_TYPE_U32)],
                    ),
                )
            ],
        )
        self.assertEqual(metadata, expected)
