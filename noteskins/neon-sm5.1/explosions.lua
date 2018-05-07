return function(button_list, stepstype, skin_params)
	local ret= {}
	local rots= {Left= 90, Down= 0, Up= 180, Right= 270}
	for i, button in ipairs(button_list) do
		local column_frame= Def.ActorFrame{
			InitCommand= function(self)
				self:rotationz(rots[button] or 0)
					:draworder(notefield_draw_order.explosion)
			end,
			Def.ActorFrame{
				Def.Sprite{
					Texture= "Explosion 5x1.png",
					InitCommand= function(self)
						self:animate(false)
					end,
					ColumnJudgmentCommand= function(self, param)
						local judgement = {
							TapNoteScore_W1= 0, TapNoteScore_W2= 1, 
							TapNoteScore_W3= 2,	TapNoteScore_W4= 3,
							TapNoteScore_W5= 4}
						local judge = judgement[param.tap_note_score or param.hold_note_score]
						if judge then
							self:setstate(judge)
						end
					end,
					HoldCommand= function(self, param)
						if param.finished then
							self:setstate(1)
						end
					end,
				},
				InitCommand= function(self)
					self:visible(false)
				end,
				ColumnJudgmentCommand= function(self, param)
					local judgement = {
							TapNoteScore_W1= true, TapNoteScore_W2= true, 
							TapNoteScore_W3= true, TapNoteScore_W4= true,
							TapNoteScore_W5= true, HoldNoteScore_Held= true}
					local judge = judgement[param.tap_note_score or param.hold_note_score]
					if judge then
						self:stoptweening()
							:diffusealpha(1.2):zoom(1.1):visible(judge)
							:accelerate(0.15):zoom(1.0):diffusealpha(0)						
							:queuecommand("hide")
						end;
				end,
				hideCommand= function(self)
					self:visible(false)
				end,
			},
			Def.Sprite{
				Texture= "Hold Explosion.png", InitCommand= function(self)
					self:visible(false):SetAllStateDelays(.1)
				end,
				HoldCommand= function(self, param)
					if param.start then
						self:finishtweening()
							:zoom(1):diffusealpha(1):visible(true)
					elseif param.finished then
						self:stopeffect():linear(0.06):diffusealpha(0)
							:sleep(0):queuecommand("hide")
					else
						self:zoom(1)
					end
				end,
				hideCommand= function(self)
					self:visible(false)
				end,
			},
		}
		ret[i]= column_frame
	end
	return ret
end
