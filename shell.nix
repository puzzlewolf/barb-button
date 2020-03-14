with import <nixpkgs> {};
stdenv.mkDerivation {
  name = "barb_button";
  buildInputs = [
    jq
  ];
}

