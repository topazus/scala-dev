my scala3 dev

cmake \
  -G Ninja \
  ../llvm \
  -DCMAKE_BUILD_TYPE=Release \
  -DFLANG_ENABLE_WERROR=On \
  -DLLVM_ENABLE_ASSERTIONS=ON \
  -DLLVM_TARGETS_TO_BUILD=host \
  -DCMAKE_INSTALL_PREFIX=$INSTALLDIR
  -DLLVM_LIT_ARGS=-v \
  -DLLVM_ENABLE_PROJECTS="clang;mlir;flang" \
  -DLLVM_ENABLE_RUNTIMES="compiler-rt"


### build llvm/clang

mkdir build && cd build

cmake -G Ninja
  \ -DCMAKE_BUILD_TYPE=Release
  \ -DLLVM_ENABLE_PROJECTS="clang;clang-tools-extra;libcxx;libcxxabi;polly;lldb;lld;compiler-rt" ../llvm
