# Copyright (c) 2015-2020 Clearmatics Technologies Ltd
#
# SPDX-License-Identifier: LGPL-3.0+

from commands.utils import create_zeth_client_and_mixer_desc, \
    load_zeth_address, open_wallet, parse_output, do_sync
from zeth.constants import JS_INPUTS, JS_OUTPUTS
from commands.constants import PROVER_SERVER_ENDPOINT_DEFAULT
from zeth.mixer_client import ZethAddressPub
from zeth.utils import EtherValue, from_zeth_units
from api.zeth_messages_pb2 import ZethNote
from click import command, option, pass_context, ClickException, Context
from typing import List, Tuple, Optional
import sys
sys.path.append('../')
from contract.Groth16Mixer import Groth16Mixer
from python_web3.eth_account.account import Account

def mix(
        mixer_addr: str,
        username: str,
        password: str,
        vin: str,
        vout: str,
        input_notes: List[str],
        output_specs: List[str]
        ) -> None:
    """
    Generic mix function
    """
    # Some sanity checks
    if len(input_notes) > JS_INPUTS:
        raise ClickException(f"too many inputs (max {JS_INPUTS})")
    if len(output_specs) > JS_OUTPUTS:
        raise ClickException(f"too many outputs (max {JS_OUTPUTS})")

    print(f"vin = {vin}")
    print(f"vout = {vout}")

    vin_pub = EtherValue(vin)
    vout_pub = EtherValue(vout)
    zeth_client = create_zeth_client_and_mixer_desc(PROVER_SERVER_ENDPOINT_DEFAULT, mixer_addr, username, password)

    zeth_address = load_zeth_address(username)
    wallet = open_wallet(
        zeth_client.mixer_instance, zeth_address.addr_sk, username)

    inputs: List[Tuple[int, ZethNote]] = [
        wallet.find_note(note_id).as_input() for note_id in input_notes]
    outputs: List[Tuple[ZethAddressPub, EtherValue]] = [
        parse_output(out_spec) for out_spec in output_specs]

    # Compute input and output value total and check that they match
    input_note_sum = from_zeth_units(
        sum([int(note.value, 16) for _, note in inputs]))
    output_note_sum = sum([value for _, value in outputs], EtherValue(0))
    if vin_pub + input_note_sum != vout_pub + output_note_sum:
        raise ClickException("input and output value mismatch")

    #eth_address = load_eth_address(eth_addr)
    fisco_bcos_address = zeth_client.mixer_instance.client.ecdsa_account.address
    # If instance uses an ERC20 token, tx_value can be 0 not default vin_pub.
    tx_value: Optional[EtherValue] = EtherValue(0)
    #if mixer_desc.token:
    #    tx_value = EtherValue(0)

    (outputresult, receipt) = zeth_client.joinsplit(
        wallet.merkle_tree,
        zeth_address.ownership_keypair(),
        fisco_bcos_address,
        inputs,
        outputs,
        vin_pub,
        vout_pub,
        tx_value)

    print("receipt output :", outputresult)
    #do_sync(wallet, receipt)
if __name__ == '__main__':
    mix()