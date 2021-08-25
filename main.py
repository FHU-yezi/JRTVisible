import sys
import time

from JianshuResearchTools.article import GetArticleAllBasicData
from JianshuResearchTools.assert_funcs import (AssertArticleUrl,
                                               AssertCollectionUrl,
                                               AssertIslandUrl,
                                               AssertNotebookUrl,
                                               AssertUserUrl)
from JianshuResearchTools.collection import GetCollectionAllBasicData
from JianshuResearchTools.exceptions import InputError
from JianshuResearchTools.island import GetIslandAllBasicData
from JianshuResearchTools.user import GetUserAllBasicData
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from article_window_ui import Ui_ArticleDataWindow
from collection_window_ui import Ui_CollectionDataWindow
from island_window_ui import Ui_IslandDataWindow
from main_window_ui import Ui_MainWindow
from notebook_data_ui import Ui_NotebookDataWindow
from user_window_ui import Ui_UserDataWindow
from JianshuResearchTools.notebook import GetNotebookAllBasicData, GetNotebookArticlesInfo

__version__ = "0.0.1"

class UserWindow(QMainWindow, Ui_UserDataWindow):
    def __init__(self, parent=None, user_url=None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.UpdateData(user_url)
    
    def UpdateData(self, user_url):
        all_data = GetUserAllBasicData(user_url)
        
        self.Version.setText(__version__)
        self.DataTime.setText(time.strftime('%Y-%m-%d %H:%M:%S'))
        
        self.setWindowTitle(self.windowTitle() + all_data["name"])
        self.UserName.setText(all_data["name"])
        if all_data["gender"] == 0:  # 未知
            self.SexUnknown.setEnabled(True)
            self.SexUnknown.setChecked(True)
        elif all_data["gender"] == 1:  # 男
            self.SexMale.setEnabled(True)
            self.SexMale.setChecked(True)
        elif all_data["gender"] == 2:  # 女
            self.SexFemale.setEnabled(True)
            self.SexFemale.setChecked(True)
        self.FollowersCount.setText(str(all_data["followers_count"]))
        self.FansCount.setText(str(all_data["fans_count"]))
        self.ArticlesCount.setText(str(all_data["articles_count"]))
        self.Wordage.setText(str(all_data["wordage"]))
        self.LikesCount.setText(str(all_data["likes_count"]))
        self.TotalAssetsCount.setText(str(all_data["assets_count"]))
        self.FPCount.setText(str(all_data["FP_count"]))
        self.FTNCount.setText(str(all_data["FTN_count"]))
        self.BadgesList.addItems(all_data["badges_list"])
        self.LastUpdateTime.setText(str(all_data["last_update_time"]))
        self.VIPLevel.setText(str(all_data["vip_info"]["vip_type"]))
        self.VIPExpireDate.setText(str(all_data["vip_info"]["expire_date"]))
        self.NextAnniversaryDay.setText(str(all_data["next_anniversary_day"]))
        self.IntroductionText.setText(all_data["introduction_text"])


class ArticleWindow(QMainWindow, Ui_ArticleDataWindow):
    def __init__(self, parent=None, url=None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.UpdateData(url)

    def UpdateData(self, article_url):
        all_data = GetArticleAllBasicData(article_url)
        
        self.Version.setText(__version__)
        self.DataTime.setText(str(time.strftime('%Y-%m-%d %H:%M:%S')))

        self.setWindowTitle(self.windowTitle() + all_data["title"])
        self.ArticleName.setText(all_data["title"])
        self.AuthorName.setText(all_data["author_name"])
        self.PublishTime.setText(str(all_data["publish_time"]))
        self.UpdateTime.setText(str(all_data["update_time"]))
        self.Wordage.setText(str(all_data["wordage"]))
        self.FPCount.setText(str(all_data["FP_count"]))
        self.LikesCount.setText(str(all_data["likes_count"]))
        self.CommentsCount.setText(str(all_data["comments_count"]))
        self.MostValuableCommentsCount.setText(str(all_data["most_valuable_comments_count"]))
        self.PaidType.setText(str(all_data["paid_status"]))
        self.CommentStatus.setText(str(all_data["comment_status"]))
        self.ReprintStatus.setText(str(all_data["reprint_status"]))
        self.ArticleContent.setText(all_data["description"])
        
        
class CollectionWindow(QMainWindow, Ui_CollectionDataWindow):
    def __init__(self, parent=None, url=None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.UpdateData(url)
    
    def UpdateData(self, collection_url):
        all_data = GetCollectionAllBasicData(collection_url)
        
        self.Version.setText(__version__)
        self.DataTime.setText(str(time.strftime('%Y-%m-%d %H:%M:%S')))

        self.setWindowTitle(self.windowTitle() + all_data["name"])
        self.CollectionName.setText(all_data["name"])
        self.ArticlesCount.setText(str(all_data["articles_count"]))
        self.SubscribersCount.setText(str(all_data["subscribers_count"]))
        self.ArticleUpdateTime.setText(str(all_data["articles_update_time"]))
        self.InformationUpdateTime.setText(str(all_data["information_update_time"]))
        self.MainEditerName.setText(str(all_data["owner_info"]["name"]))
        self.CollectionIntroduction.setText(all_data["introduction_text"])
        
class IslandWindow(QMainWindow, Ui_IslandDataWindow):
    def __init__(self, parent=None, url=None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.UpdateData(url)
    
    def UpdateData(self, island_url):
        all_data = GetIslandAllBasicData(island_url)
        
        self.Version.setText(__version__)
        self.DataTime.setText(str(time.strftime('%Y-%m-%d %H:%M:%S')))

        self.setWindowTitle(self.windowTitle() + all_data["name"])
        self.IslandName.setText(all_data["name"])
        self.IslandCategory.setText(all_data["category"])
        self.IslandMembersCount.setText(str(all_data["members_count"]))
        self.PostsCount.setText(str(all_data["posts_count"]))
        self.IslandMasterName.setDisabled(True)
        self.IslandMasterName.setText("开发中......")  # TODO
        self.IslandIntroduction.setText(all_data["introduction"])
        
class NotebookWindow(QMainWindow, Ui_NotebookDataWindow):
    def __init__(self, parent=None, url=None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.UpdateData(url)
    
    def UpdateData(self, notebook_url):
        all_data = GetNotebookAllBasicData(notebook_url)
        
        self.Version.setText(__version__)
        self.DataTime.setText(str(time.strftime('%Y-%m-%d %H:%M:%S')))

        self.setWindowTitle(self.windowTitle() + all_data["name"])
        self.NotebookName.setText(all_data["name"])
        self.Author.setText(all_data["author_info"]["name"])
        self.ArticlesCount.setText(str(all_data["articles_count"]))
        self.TotalWordage.setText(str(all_data["wordage"]))
        self.SubscribersCount.setText(str(all_data["subscribers_count"]))
        self.UpdateTime.setText(str(all_data["update_time"]))
        self.RecentlyArticles.addItems([item["title"] for item in GetNotebookArticlesInfo(notebook_url)])


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
            "用户": AssertUserUrl, 
            "文章": AssertArticleUrl, 
            "专题": AssertCollectionUrl, 
            "小岛": AssertIslandUrl, 
            "文集": AssertNotebookUrl, 
        }
        if selected_url_type == "自动检测":
            for url_type, assert_func in type_to_assert.items():
                try:
                    assert_func(url)
                except InputError:
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
            except InputError:  # Url 与选择的类型不匹配
                QMessageBox.critical(self, "链接错误", "您输入的链接与选择类型不匹配，请检查")
                return
            else:
                window_obj = type_to_window_obj[selected_url_type](self, url)
                window_obj.show()
        
        
app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
