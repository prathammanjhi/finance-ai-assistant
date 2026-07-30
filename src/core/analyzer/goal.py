from datetime import datetime
import pandas as pd
import math

def calculate_goals(goals):
    goal_analysis = []

    for index, goal in goals.iterrows():
        # 1. Extract values
        goal_name = goal["Goal"]
        goal_type = goal["Type"]
        target_amount = goal["Target Amount"]
        current_amount = goal["Current Amount"]
        target_date = goal["Target Date"]
        priority = goal["Priority"]
        status = goal["Status"]

        # 2. Calculations
        remaining_amount = max(0, target_amount - current_amount)
        progress_percentage = round(
            min(100, max(0, (current_amount / target_amount) * 100))
            if target_amount > 0
            else 0,
            2,
        )
        today = datetime.today()
        days_remaining = (target_date - today).days
        months_remaining = max(0, math.ceil(days_remaining / 30))
        required_monthly_contribution = math.ceil(remaining_amount / months_remaining)

        # 3. Append dictionary
        goal_analysis.append(
            {
                "goal": goal_name,
                "type": goal_type,
                "target_amount": target_amount,
                "current_amount": current_amount,
                "remaining_amount": remaining_amount,
                "progress_percentage": progress_percentage,
                "target_date": target_date,
                "priority": priority,
                "status": status,
                "months_remaining": months_remaining,
                "required_monthly_contribution": required_monthly_contribution,
            }
        )

    # ============================
    # Goal Portfolio Summary
    # ============================

    total_goals = len(goals)

    active_goals = len(goals.loc[goals["Status"] == "Active"])

    completed_goals = len(goals.loc[goals["Status"] == "Completed"])

    paused_goals = len(goals.loc[goals["Status"] == "Paused"])

    cancelled_goals = len(goals.loc[goals["Status"] == "Cancelled"])

    completion_rate = (completed_goals / total_goals) * 100 if total_goals > 0 else 0

    active_goal_rate = (active_goals / total_goals) * 100 if total_goals > 0 else 0

    total_target_amount = goals["Target Amount"].sum()

    total_current_amount = goals["Current Amount"].sum()

    total_remaining_amount = max(0, total_target_amount - total_current_amount)

    overall_progress_percentage = round(
        min(100, max(0, (total_current_amount / total_target_amount) * 100))
        if total_target_amount > 0
        else 0,
        2,
    )

    goal_summary = {
        # Goal Counts
        "total_goals": total_goals,
        "active_goals": active_goals,
        "completed_goals": completed_goals,
        "paused_goals": paused_goals,
        "cancelled_goals": cancelled_goals,
        # Goal Rates
        "completion_rate": completion_rate,
        "active_goal_rate": active_goal_rate,
        # Financial Totals
        "total_target_amount": total_target_amount,
        "total_current_amount": total_current_amount,
        "total_remaining_amount": total_remaining_amount,
        # Portfolio Progress
        "overall_progress_percentage": overall_progress_percentage,
    }

    return goal_analysis, goal_summary

def generate_goal_insights(goal_analysis):
    goal_insights = []
    for goal in goal_analysis:
        goal_name = goal["goal"]
        progress = goal["progress_percentage"]
        months_remaining = goal["months_remaining"]
        goal_priority = goal["priority"]
        status = goal["status"]

        if status == "Completed":
            insight_status = "Completed"
            insight_priority = "None"
            reason = "Goal has been achieved."
            recommendation = "Create a new financial goal."

        elif progress < 20 and months_remaining <= 3:
            insight_status = "Critical"
            insight_priority = "High"
            reason = "Goal is significantly behind schedule."
            recommendation = "Increase monthly contribution immediately."

        elif progress < 50 and goal_priority == "High":
            insight_status = "Critical"
            insight_priority = "High"
            reason = "Goal progress is below expected pace."
            recommendation = "Increase monthly savings toward this goal."

        elif progress < 50 and goal_priority == "Medium":
            insight_status = "Behind"
            insight_priority = "Medium"
            reason = "Goal progress is below expected pace."
            recommendation = "Increase monthly savings toward this goal."

        elif progress < 50:
            insight_status = "Behind"
            insight_priority = "Medium"
            reason = "Goal progress is below expected pace."
            recommendation = "Increase monthly savings toward this goal."

        elif goal_priority == "High":
            insight_status = "Behind"
            insight_priority = "Medium"
            reason = "Goal progress is below expected pace."
            recommendation = "Increase monthly savings toward this goal."

        else:
            insight_status = "On Track"
            insight_priority = "Normal"
            reason = "Goal is progressing steadily."
            recommendation = "Continue current contribution."

        goal_insights.append(
            {
                "goal": goal_name,
                "goal_priority": goal_priority,
                "status": insight_status,
                "priority": insight_priority,
                "reason": reason,
                "recommendation": recommendation,
            }
        )
    return goal_insights

def generate_goal_snapshot(
    goal_analysis,
    goal_summary,
    goal_insights,
):
    goal_snapshot = {
        "goal_analysis": goal_analysis,
        "goal_summary": goal_summary,
        "goal_insights": goal_insights,
    }

    return goal_snapshot