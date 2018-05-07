return function(button_list, stepstype, skin_parameters)
	local ret= {}
	local rots= {Left= 90, Down= 0, Up= 180, Right= 270}
	for i, button in ipairs(button_list) do
		ret[i]= Def.Sprite{
			Texture= "Receptor 4x1 (doubleres).png", InitCommand= function(self)
				self:rotationz(rots[button] or 0):SetAllStateDelays(1)
					:effectclock("beat"):diffuseramp()
					:effectcolor1(0.1,0.1,0.1,1):effectcolor2(1,1,1,1)
					:effectperiod(0.5):effecttiming(0.25,0.50,0,0.25):effectoffset(-0.25)
					:draworder(notefield_draw_order.receptor)
			end,
			WidthSetCommand= function(self, param)
				param.column:set_layer_fade_type(self, "FieldLayerFadeType_Receptor")
			end,
			ColumnJudgmentCommand= function(self)
				self.none = false
			end,
			BeatUpdateCommand= function(self, param)
				if param.pressed then
					if self.none == true then
						if self.onepress == true then
							self:stoptweening():zoom(.75):linear(.11):zoom(1)
							self.onepress = false
						end
					end
				else
					self:zoom(1)
					self.onepress = true
					self.none = true
				end
			end,
		}
	end
	return ret
end
