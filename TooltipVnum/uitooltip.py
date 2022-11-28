# in uitooltip.py search

	def AddItemData(self, itemVnum, metinSlot, attrSlot = 0, flags = 0, unbindTime = 0):
		self.itemVnum = itemVnum
		item.SelectItem(itemVnum)
		itemType = item.GetItemType()
		itemSubType = item.GetItemSubType()

# add above of the last self.ShowToolTip()

		if chr.IsGameMaster(player.GetMainCharacterIndex()):
			self.AppendTextLine("VNUM: %i" %itemVnum)