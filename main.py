import sys
import time

import JianshuResearchTools as jrt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from article_window_ui import Ui_ArticleDataWindow
from collection_window_ui import Ui_CollectionDataWindow
from island_window_ui import Ui_IslandDataWindow
from main_window_ui import Ui_MainWindow
from notebook_data_ui import Ui_NotebookDataWindow
from user_window_ui import Ui_UserDataWindow

__version__ = "0.0.1"

class UserWindow(QMainWindow, Ui_UserDataWindow):
    def __init__(self, parent=None, url=None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)

        data = self.GetData(url)
        self.UpdateData(data)
        
    
    def GetData(self, user_url):
        result = {}
        result["user_name"] = jrt.user.GetUserName(user_url)
        result["sex"] = {
            0: "未知", 
            1: "男", 
            2: "女"}[jrt.user.GetUserGender(user_url)]
        result["followers_count"] = jrt.user.GetUserFollowersCount(user_url)
        result["fans_count"] = jrt.user.GetUserFansCount(user_url)
        result["articles_count"] = jrt.user.GetUserArticlesCount(user_url)
        result["total_wordage"] = jrt.user.GetUserWordage(user_url)
        result["likes_count"] = jrt.user.GetUserLikesCount(user_url)
        result["total_assets_count"] = jrt.user.GetUserAssetsCount(user_url)
        result["fp_count"] = jrt.user.GetUserFPCount(user_url)
        result["ftn_count"] = jrt.user.GetUserFTNCount(user_url)
        result["badges_list"] = jrt.user.GetUserBadgesList(user_url)
        result["last_update_time"] = jrt.user.GetUserLastUpdateTime(user_url)
        result["vip_level"] = jrt.user.GetUserVIPInfo(user_url)["vip_type"]
        result["vip_expire_date"] = jrt.user.GetUserVIPInfo(user_url)["expire_date"]
        # TODO: 等待 JRT 实现
        # result["next_anniversary_day"] = jrt.user.GetUserNextAnniversaryDay(user_url)
        result["self_introduction"] = jrt.user.GetUserIntroductionText(user_url)
        return result
    
    def UpdateData(self, data):
        self.Version.setText(__version__)
        self.DataTime.setText(time.strftime('%Y-%m-%d %H:%M:%S'))
        
        self.setWindowTitle(self.windowTitle() + data["user_name"])
        self.UserName.setText(data["user_name"]) 
        if data["sex"] == "未知":
            self.SexUnknown.setEnabled(True)
            self.SexUnknown.setChecked(True)
        elif data["sex"] == "男":
            self.SexMale.setEnabled(True)
            self.SexMale.setChecked(True)
        elif data["sex"] == "女":
            self.SexFemale.setEnabled(True)
            self.SexFemale.setChecked(True)
        self.FollowersCount.setText(str(data["followers_count"]))
        self.FansCount.setText(str(data["fans_count"]))
        self.ArticlesCount.setText(str(data["articles_count"]))
        self.Wordage.setText(str(data["total_wordage"]))
        self.LikesCount.setText(str(data["likes_count"]))
        self.TotalAssetsCount.setText(str(data["total_assets_count"]))
        self.FPCount.setText(str(data["fp_count"]))
        self.FTNCount.setText(str(data["ftn_count"]))
        self.BadgesList.addItems(data["badges_list"])
        self.LastUpdateTime.setText(str(data["last_update_time"]))
        self.VIPLevel.setText(str(data["vip_level"]))
        self.VIPExpireDate.setText(str(data["vip_expire_date"]))
        # TODO: 等待 JRT 实现
        # self.NextAnniversaryDay.setText(data["next_anniversary_day"])
        self.IntroductionText.setText(data["self_introduction"])


class ArticleWindow(QMainWindow, Ui_ArticleDataWindow):
    def __init__(self, parent=None, url=None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)

        data = self.GetData(url)
        self.UpdateData(data)
    
    def GetData(self, article_url):
        result = {}
        result["article_title"] = jrt.article.GetArticleTitle(article_url)  # TODO: 变量名修改
        result["author_name"] = jrt.article.GetArticleAuthorName(article_url)
        result["publish_time"] = jrt.article.GetArticlePublishTime(article_url)
        result["update_time"] = jrt.article.GetArticleUpdateTime(article_url)
        result["wordage"] = jrt.article.GetArticleWordage(article_url)
        result["FP_count"] = jrt.article.GetArticleTotalFPCount(article_url)
        result["likes_count"] = jrt.article.GetArticleLikesCount(article_url)
        result["comments_count"] = jrt.article.GetArticleCommentsCount(article_url)
        result["most_valuable_comments_count"] = jrt.article.GetArticleMostValuableCommentsCount(article_url)
        result["paid_type"] = jrt.article.GetArticlePaidStatus(article_url)
        result["comment_status"] = jrt.article.GetArticleCommentStatus(article_url)
        result["reprint_status"] = jrt.article.GetArticleReprintStatus(article_url)
        result["article_content"] = jrt.article.GetArticleText(article_url)
        return result

    def UpdateData(self, data):
        self.Version.setText(__version__)
        self.DataTime.setText(str(time.strftime('%Y-%m-%d %H:%M:%S')))

        self.setWindowTitle(self.windowTitle() + data["article_title"])
        self.ArticleName.setText(data["article_title"])
        self.AuthorName.setText(data["author_name"])
        self.PublishTime.setText(str(data["publish_time"]))
        self.UpdateTime.setText(str(data["update_time"]))
        self.Wordage.setText(str(data["wordage"]))
        self.FPCount.setText(str(data["FP_count"]))
        self.LikesCount.setText(str(data["likes_count"]))
        self.CommentsCount.setText(str(data["comments_count"]))
        self.MostValuableCommentsCount.setText(str(data["most_valuable_comments_count"]))
        self.PaidType.setText(str(data["paid_type"]))
        self.CommentStatus.setText(str(data["comment_status"]))
        self.ReprintStatus.setText(str(data["reprint_status"]))
        self.ArticleContent.setText(data["article_content"])
        
        
class CollectionWindow(QMainWindow, Ui_CollectionDataWindow):
    def __init__(self, parent=None, url=None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)

        data = self.GetData(url)
        self.UpdateData(data)
    
    def GetData(self, url):
        pass
    
    def UpdateData(self, data):
        pass
        
class IslandWindow(QMainWindow, Ui_IslandDataWindow):
    def __init__(self, parent=None, url=None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)

        data = self.GetData(url)
        self.UpdateData(data)
    
    def GetData(self, url):
        pass
    
    def UpdateData(self, data):
        pass
        
class NotebookWindow(QMainWindow, Ui_NotebookDataWindow):
    def __init__(self, parent=None, url=None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)

        data = self.GetData(url)
        self.UpdateData(data)
    
    def GetData(self, url):
        pass
    
    def UpdateData(self, data):
        pass


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.GetDataButton.clicked.connect(self.GetDataButtonClicked)
    def GetDataButtonClicked(self):
        selected_url_type = self.UrlType.currentText()
        url = self.UrlInput.text()
        type_to_window_obj = {
            "用户": UserWindow, 
            "文章": ArticleWindow, 
            "专题": CollectionWindow, 
            "小岛": IslandWindow, 
            "文集": NotebookWindow, 
        }
        type_to_assert = {
            "用户": jrt.assert_funcs.AssertUserUrl, 
            "文章": jrt.assert_funcs.AssertArticleUrl, 
            "专题": jrt.assert_funcs.AssertCollectionUrl, 
            "小岛": jrt.assert_funcs.AssertIslandUrl, 
            "文集": jrt.assert_funcs.AssertNotebookUrl, 
        }
        if selected_url_type == "自动检测":
            for url_type, assert_func in type_to_assert.items():
                try:
                    assert_func(url)
                except jrt.exceptions.InputError:
                    pass
                else:  # 满足断言条件
                    window_obj = type_to_window_obj[url_type](self, url)
                    window_obj.show()
                    break
            else:  # 不满足任何条件
                QMessageBox.critical(self, "链接错误", "您输入的链接无效，请检查")
        else:  # 没有选择自动检测
            try:
                type_to_assert[selected_url_type](url)  # 对输入的 Url 进行断言
            except jrt.exceptions.InputError:  # Url 与选择的类型不匹配
                QMessageBox.critical(self, "链接错误", "您输入的链接与选择类型不匹配，请检查")
                return
            else:
                window_obj = type_to_window_obj[selected_url_type](self, url)
                window_obj.show()
        
        
app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
