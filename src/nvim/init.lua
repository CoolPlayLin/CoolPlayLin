-- Packer
require("plugins.plugins-setup")

-- plugins
require("plugins.lualine")
require("plugins.nvim-tree")
require("plugins.lsp")
require("plugins.cmp")
require("plugins.comment")
require("plugins.autopairs")
require("plugins.gitsigns")
require("plugins.bufferline")
require("plugins.telescope")
require("plugins.treesitter")
require("plugins.toggleterm")

-- options
require("core.options")
require("core.keymaps")