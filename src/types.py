import ctypes


# Bsic types
ELF32_Addr		= ctypes.c_uint32
ELF32_Half		= ctypes.c_uint16
ELF32_Off		= ctypes.c_uint32
ELF32_Sword		= ctypes.c_int32
ELF32_Word		= ctypes.c_uint32

ELF64_Addr		= ctypes.c_uint64
ELF64_Half		= ctypes.c_uint16
ELF64_Off		= ctypes.c_uint64
ELF64_Sword		= ctypes.c_int32
ELF64_Word		= ctypes.c_uint32
ELF64_Xword		= ctypes.c_uint64
ELF64_Sxword	= ctypes.c_int64


# e_ident[] needed types
EI_MAG0 	= 0			# File identification
EI_MAG1 	= 1			# File identification
EI_MAG2 	= 2			# File identification
EI_MAG3 	= 3			# File identification
EI_CLASS	= 4			# File class
EI_DATA		= 5			# Data encoding
EI_VERSION	= 6			# File version
EI_PAD 	  	= 7			# Start of padding bytes
EI_NIDENT 	= 16		# Size of e_ident[]

MAGIC 		= '\x7fELF' # ELF magic

	# ELF classes
ELFCLASSNONE = 0		# Invalid class
ELFCLASS32 	 = 1		# 32-bit class
ELFCLASS64	 = 2		# 64-bit class

